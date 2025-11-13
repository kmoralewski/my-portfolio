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
    public partial class UpdateUser : Form
    {
        public UpdateUser()
        {
            InitializeComponent();
        }

        private void UpdateUser_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'gbdataDataSet1.USERS' table. You can move, or remove it, as needed.
            this.uSERSTableAdapter1.Fill(this.gbdataDataSet1.USERS);
            // TODO: This line of code loads data into the 'gbdataDataSet1.WAREHOUSE' table. You can move, or remove it, as needed.
            this.wAREHOUSETableAdapter.Fill(this.gbdataDataSet1.WAREHOUSE);


        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (var conn = new SqlConnection(@"Data Source = DESKTOP-4UQ150R\MYSQL1; Initial Catalog = gbdata; Integrated Security = True"))
            {
                try
                {
                    conn.Open();
                    string sql = "insert into users values (@user_id,@username,@password,@firstname,@lastname,@role);";
                    using (var cmd = new SqlCommand(sql, conn))
                    {
                        cmd.Parameters.AddWithValue("@user_id", textbox1.Text);
                        cmd.Parameters.AddWithValue("@username", textBox2.Text);
                        cmd.Parameters.AddWithValue("@password", textBox3.Text);
                        cmd.Parameters.AddWithValue("@firstname", textBox4.Text);
                        cmd.Parameters.AddWithValue("@lastname", textBox5.Text);
                        cmd.Parameters.AddWithValue("@role", textBox6.Text);
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

        private void button2_Click(object sender, EventArgs e)
        {
            using (var conn = new SqlConnection(@"Data Source = DESKTOP-4UQ150R\MYSQL1; Initial Catalog = gbdata; Integrated Security = True"))
            {
                try
                {
                    conn.Open();
                    string sql = "delete from users where user_id= (@user_id)";
                    using (var cmd = new SqlCommand(sql, conn))
                    {
                        cmd.Parameters.AddWithValue("@user_id", textBox7.Text);
                        cmd.ExecuteNonQuery();
                    }
                    MessageBox.Show("Success");
                    this.Close();
                    
                }
                catch
                {
                    MessageBox.Show("Unsuccessful");
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
