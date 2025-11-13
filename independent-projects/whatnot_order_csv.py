import os
import csv
import pyautogui
from paddleocr import PaddleOCR
from datetime import datetime

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Screenshot region for Whatnot order
region = {"top": 155, "left": 1525, "width": 355, "height": 795}
screenshot_folder = "order_screenshots"

def get_next_index(folder):
    """Return the next index for whatnot{i}.png"""
    existing = [f for f in os.listdir(folder) if f.startswith("whatnot") and f.endswith(".png")]
    indexes = [int(f.replace("whatnot", "").replace(".png", "")) for f in existing if f.replace("whatnot", "").replace(".png", "").isdigit()]
    return max(indexes, default=0) + 1

def take_screenshot_and_save(folder=screenshot_folder):
    """Takes a screenshot and saves it as whatnot{i}.png"""
    if not os.path.exists(folder):
        os.makedirs(folder)
    i = get_next_index(folder)
    filename = f"whatnot{i}.png"
    path = os.path.join(folder, filename)
    screenshot = pyautogui.screenshot(region=(region["left"], region["top"], region["width"], region["height"]))
    screenshot.save(path)
    print(f"📸 Saved screenshot: {path}")
    return path

def extract_order_details(text):
    lines = text.split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    def get_value(key):
        try:
            idx = [i for i, l in enumerate(lines) if l.lower() == key.lower()][0]
            return lines[idx + 1].strip()
        except (IndexError, ValueError):
            return ""

    raw_date = get_value("Order date")
    try:
        parsed_date = datetime.strptime(raw_date, "%b %d, %Y")
        order_date = parsed_date.strftime("%#m/%#d/%Y")  # Windows-friendly format
    except ValueError:
        order_date = raw_date

    order_time = get_value("Order time")
    buyer = get_value("Buyer")
    category = get_value("Category")
    quantity = get_value("Quantity")
    title = get_value("Livestream")
    price = get_value("Price")
    shipping = get_value("Shipping paid by buyer")
    total = get_value("Order total")
    commission = get_value("Commission")
    processing = get_value("Payment processing fee")
    shipping_fee = get_value("Shipping")
    earnings = get_value("Net earnings")

    return [
        order_date, order_time, buyer, category, quantity,
        title, price, shipping, total,
        commission, processing, shipping_fee, earnings
    ]


def save_to_csv(data_list, filename="orders.csv"):
    if not data_list:
        return

    headers = [
        "Order Date", "Order Time", "Buyer", "Category", "Quantity",
        "Title", "Price", "Shipping", "Order Total",
        "Commission", "Processing Fee", "Shipping Fee", "Net Earnings"
    ]

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(headers)
        for row in data_list:
            writer.writerow(row)

def process_single_image(image_path):
    result = ocr.ocr(image_path, cls=True)
    text_lines = [line[1][0] for line in result[0]]
    text = "\n".join(text_lines)

    parsed = extract_order_details(text)  # Returns a list
    os.remove(image_path)
    print(f"🗑️ Deleted processed image: {image_path}")
    return [parsed]  # Wrap in list to match save_to_csv input


# Run this part
if __name__ == "__main__":
    while True:
        input("Go?")
        image_path = take_screenshot_and_save()
        data = process_single_image(image_path)
        save_to_csv(data)
        print("✅ Order saved to CSV.")

