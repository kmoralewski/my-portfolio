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
    public partial class CheckIn : Form
    {

        public CheckIn()
        {
            InitializeComponent();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void CheckIn_Load(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection(@"Data Source = DESKTOP-4UQ150R\MYSQL1; Initial Catalog = gbdata; Integrated Security = True"); 
            SqlDataAdapter sda = new SqlDataAdapter("SELECT COUNT(*) FROM inventory WHERE toolid='" + textBox2.Text + "'", con);
            DataTable dt = new DataTable(); 
            sda.Fill(dt);
            if (dt.Rows[0][0].ToString() == "1")
            {
                
                this.Hide();
                MessageBox.Show("Success");
            }
            else
            {
                MessageBox.Show("Invalid TOOLID");
            }
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
