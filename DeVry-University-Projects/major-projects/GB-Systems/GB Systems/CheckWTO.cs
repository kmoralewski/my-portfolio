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
    public partial class CheckWTO : Form
    {
        public CheckWTO()
        {
            InitializeComponent();
        }

        private void CheckWTO_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'gbdataDataSet1.INVENTORY' table. You can move, or remove it, as needed.
            this.iNVENTORYTableAdapter1.Fill(this.gbdataDataSet1.INVENTORY);


        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
