using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace WindowsFormsConnectSQLServertoCSharp
{
    public partial class Login : Form
    {
        public MainMenu MainMenu = new MainMenu(); 
        public Login()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection(@"Data Source = DESKTOP-4UQ150R\MYSQL1; Initial Catalog = gbdata; Integrated Security = True"); 
            SqlDataAdapter sda = new SqlDataAdapter("SELECT COUNT(*) FROM users WHERE username='" + txtUsername.Text + "' AND password='" + txtPassword.Text + "'", con);
            DataTable dt = new DataTable();
            sda.Fill(dt);
            if (dt.Rows[0][0].ToString() == "1")
            {
                this.Hide();
                MainMenu.ShowDialog();
            }
            else
            {
                MessageBox.Show("Invalid username or password");
            }
        }
        
        

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            this.Hide();
            MainMenu.ShowDialog();
        }

        private void Login_Load(object sender, EventArgs e)
        {

        }
    }
}
