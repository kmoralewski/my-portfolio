using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsConnectSQLServertoCSharp
{
    public partial class CheckInv : Form
    {
        public CheckInv()
        {
            InitializeComponent();
        }

        private void CheckInv_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'gbdataDataSet1.INVENTORY' table. You can move, or remove it, as needed.
            this.iNVENTORYTableAdapter1.Fill(this.gbdataDataSet1.INVENTORY);
            // TODO: This line of code loads data into the 'gbdataDataSet.INVENTORY' table. You can move, or remove it, as needed.
            this.iNVENTORYTableAdapter.Fill(this.gbdataDataSet.INVENTORY);

        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void dataGridView1_CellContentClick_1(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
