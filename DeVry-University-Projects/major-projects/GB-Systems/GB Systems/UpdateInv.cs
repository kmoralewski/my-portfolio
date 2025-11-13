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
    public partial class UpdateInv : Form
    {
        public UpdateInv()
        {
            InitializeComponent();
        }

        private void UpdateInv_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'gbdataDataSet1.INVENTORY' table. You can move, or remove it, as needed.
            this.iNVENTORYTableAdapter1.Fill(this.gbdataDataSet1.INVENTORY);


        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (var conn = new SqlConnection(@"Data Source = DESKTOP-4UQ150R\MYSQL1; Initial Catalog = gbdata; Integrated Security = True"))
            {
                try
                {
                    conn.Open();
                    string sql = "insert into inventory values (@toolid,@toolname,@quantity,@availibility,@warehouse,@checkoutbyuserid);";
                    using (var cmd = new SqlCommand(sql, conn))
                    {
                        cmd.Parameters.AddWithValue("@toolid", textbox1.Text);
                        cmd.Parameters.AddWithValue("@toolname", textBox2.Text);
                        cmd.Parameters.AddWithValue("@quantity", textBox3.Text);
                        cmd.Parameters.AddWithValue("@availibility", textBox4.Text);
                        cmd.Parameters.AddWithValue("@warehouse", textBox5.Text);
                        cmd.Parameters.AddWithValue("@checkoutbyuserid", textBox6.Text);
                        cmd.ExecuteNonQuery();
                        MessageBox.Show("Success");
                        this.Close();
                    }
                }
                catch 
                {
                    MessageBox.Show("Unsuccessful");
                }
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            using (var conn = new SqlConnection(@"Data Source = DESKTOP-4UQ150R\MYSQL1; Initial Catalog = gbdata; Integrated Security = True"))
            {
                try
                {
                    conn.Open();
                    string sql = "delete from inventory where toolid= (@toolid)";
                    using (var cmd = new SqlCommand(sql, conn))
                    {
                        cmd.Parameters.AddWithValue("@toolid", textBox7.Text);
                        cmd.ExecuteNonQuery();
                        MessageBox.Show("Success");
                        this.Close();
                    }

                }
                catch
                {
                    MessageBox.Show("Unsuccessful");
                }
            }
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
