
namespace WindowsFormsConnectSQLServertoCSharp
{
    partial class CheckWTO
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.inventoryBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.gb_dataDataSet = new WindowsFormsConnectSQLServertoCSharp.gb_dataDataSet();
            this.inventoryTableAdapter = new WindowsFormsConnectSQLServertoCSharp.gb_dataDataSetTableAdapters.inventoryTableAdapter();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.tOOLIDDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.tOOLNAMEDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.cHECKOUTBYUSERIDDataGridViewTextBoxColumn = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.iNVENTORYBindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.gbdataDataSet1 = new WindowsFormsConnectSQLServertoCSharp.gbdataDataSet1();
            this.iNVENTORYTableAdapter1 = new WindowsFormsConnectSQLServertoCSharp.gbdataDataSet1TableAdapters.INVENTORYTableAdapter();
            this.button3 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.inventoryBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.gb_dataDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.iNVENTORYBindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.gbdataDataSet1)).BeginInit();
            this.SuspendLayout();
            // 
            // inventoryBindingSource
            // 
            this.inventoryBindingSource.DataMember = "inventory";
            this.inventoryBindingSource.DataSource = this.gb_dataDataSet;
            // 
            // gb_dataDataSet
            // 
            this.gb_dataDataSet.DataSetName = "gb_dataDataSet";
            this.gb_dataDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // inventoryTableAdapter
            // 
            this.inventoryTableAdapter.ClearBeforeFill = true;
            // 
            // dataGridView1
            // 
            this.dataGridView1.AutoGenerateColumns = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.tOOLIDDataGridViewTextBoxColumn,
            this.tOOLNAMEDataGridViewTextBoxColumn,
            this.cHECKOUTBYUSERIDDataGridViewTextBoxColumn});
            this.dataGridView1.DataSource = this.iNVENTORYBindingSource1;
            this.dataGridView1.Location = new System.Drawing.Point(209, 46);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.Size = new System.Drawing.Size(345, 225);
            this.dataGridView1.TabIndex = 0;
            // 
            // tOOLIDDataGridViewTextBoxColumn
            // 
            this.tOOLIDDataGridViewTextBoxColumn.DataPropertyName = "TOOLID";
            this.tOOLIDDataGridViewTextBoxColumn.HeaderText = "TOOLID";
            this.tOOLIDDataGridViewTextBoxColumn.Name = "tOOLIDDataGridViewTextBoxColumn";
            // 
            // tOOLNAMEDataGridViewTextBoxColumn
            // 
            this.tOOLNAMEDataGridViewTextBoxColumn.DataPropertyName = "TOOLNAME";
            this.tOOLNAMEDataGridViewTextBoxColumn.HeaderText = "TOOLNAME";
            this.tOOLNAMEDataGridViewTextBoxColumn.Name = "tOOLNAMEDataGridViewTextBoxColumn";
            // 
            // cHECKOUTBYUSERIDDataGridViewTextBoxColumn
            // 
            this.cHECKOUTBYUSERIDDataGridViewTextBoxColumn.DataPropertyName = "CHECKOUTBYUSERID";
            this.cHECKOUTBYUSERIDDataGridViewTextBoxColumn.HeaderText = "CHECKOUTBY";
            this.cHECKOUTBYUSERIDDataGridViewTextBoxColumn.Name = "cHECKOUTBYUSERIDDataGridViewTextBoxColumn";
            // 
            // iNVENTORYBindingSource1
            // 
            this.iNVENTORYBindingSource1.DataMember = "INVENTORY";
            this.iNVENTORYBindingSource1.DataSource = this.gbdataDataSet1;
            // 
            // gbdataDataSet1
            // 
            this.gbdataDataSet1.DataSetName = "gbdataDataSet1";
            this.gbdataDataSet1.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // iNVENTORYTableAdapter1
            // 
            this.iNVENTORYTableAdapter1.ClearBeforeFill = true;
            // 
            // button3
            // 
            this.button3.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button3.Location = new System.Drawing.Point(341, 314);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 37);
            this.button3.TabIndex = 34;
            this.button3.Text = "Exit";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // CheckWTO
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.dataGridView1);
            this.Name = "CheckWTO";
            this.Text = "CheckWhatToolOut";
            this.Load += new System.EventHandler(this.CheckWTO_Load);
            ((System.ComponentModel.ISupportInitialize)(this.inventoryBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.gb_dataDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.iNVENTORYBindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.gbdataDataSet1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion
        private gb_dataDataSet gb_dataDataSet;
        private System.Windows.Forms.BindingSource inventoryBindingSource;
        private gb_dataDataSetTableAdapters.inventoryTableAdapter inventoryTableAdapter;
        private System.Windows.Forms.DataGridView dataGridView1;
        private gbdataDataSet1 gbdataDataSet1;
        private System.Windows.Forms.BindingSource iNVENTORYBindingSource1;
        private gbdataDataSet1TableAdapters.INVENTORYTableAdapter iNVENTORYTableAdapter1;
        private System.Windows.Forms.DataGridViewTextBoxColumn tOOLIDDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn tOOLNAMEDataGridViewTextBoxColumn;
        private System.Windows.Forms.DataGridViewTextBoxColumn cHECKOUTBYUSERIDDataGridViewTextBoxColumn;
        private System.Windows.Forms.Button button3;
    }
}