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
    public partial class MainMenu : Form
    {
        public UpdateUser UpdateUser = new UpdateUser();
        public CheckInv CheckInv = new CheckInv();
        public UpdateInv UpdateInv = new UpdateInv();
        public CheckWTO CheckWTO = new CheckWTO();
        public CheckOut CheckOut = new CheckOut();
        public CheckIn CheckIn = new CheckIn();
    
        public MainMenu()
        {
            InitializeComponent();
        }

        private void MainMenu_Load(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            UpdateUser.ShowDialog();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            CheckInv.ShowDialog();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            UpdateInv.ShowDialog();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            CheckWTO.ShowDialog();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            CheckOut.ShowDialog();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            CheckIn.ShowDialog();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
