namespace student_managment
{
    partial class duzey_bul_cont
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

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle1 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle2 = new System.Windows.Forms.DataGridViewCellStyle();
            this.duzey_box = new System.Windows.Forms.ComboBox();
            this.datatable = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.görüntüle_btn = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.datatable)).BeginInit();
            this.SuspendLayout();
            // 
            // duzey_box
            // 
            this.duzey_box.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.duzey_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.duzey_box.FormattingEnabled = true;
            this.duzey_box.Items.AddRange(new object[] {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12"});
            this.duzey_box.Location = new System.Drawing.Point(352, 58);
            this.duzey_box.Name = "duzey_box";
            this.duzey_box.Size = new System.Drawing.Size(80, 32);
            this.duzey_box.TabIndex = 13;
            // 
            // datatable
            // 
            this.datatable.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.AllCells;
            this.datatable.AutoSizeRowsMode = System.Windows.Forms.DataGridViewAutoSizeRowsMode.AllCells;
            dataGridViewCellStyle1.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle1.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle1.Font = new System.Drawing.Font("Microsoft Sans Serif", 21F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            dataGridViewCellStyle1.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle1.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle1.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle1.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.datatable.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle1;
            this.datatable.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewCellStyle2.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle2.BackColor = System.Drawing.SystemColors.Window;
            dataGridViewCellStyle2.Font = new System.Drawing.Font("Microsoft Sans Serif", 21F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            dataGridViewCellStyle2.ForeColor = System.Drawing.SystemColors.ControlText;
            dataGridViewCellStyle2.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle2.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle2.WrapMode = System.Windows.Forms.DataGridViewTriState.False;
            this.datatable.DefaultCellStyle = dataGridViewCellStyle2;
            this.datatable.Location = new System.Drawing.Point(49, 108);
            this.datatable.Name = "datatable";
            this.datatable.Size = new System.Drawing.Size(725, 405);
            this.datatable.TabIndex = 21;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.Location = new System.Drawing.Point(210, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(383, 37);
            this.label1.TabIndex = 22;
            this.label1.Text = "Sınıf Düzeyini Görüntüle";
            // 
            // görüntüle_btn
            // 
            this.görüntüle_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.görüntüle_btn.Location = new System.Drawing.Point(330, 519);
            this.görüntüle_btn.Name = "görüntüle_btn";
            this.görüntüle_btn.Size = new System.Drawing.Size(148, 53);
            this.görüntüle_btn.TabIndex = 23;
            this.görüntüle_btn.Text = "Görüntüle";
            this.görüntüle_btn.UseVisualStyleBackColor = true;
            this.görüntüle_btn.Click += new System.EventHandler(this.görüntüle_btn_Click);
            // 
            // duzey_bul_cont
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.görüntüle_btn);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.datatable);
            this.Controls.Add(this.duzey_box);
            this.Name = "duzey_bul_cont";
            this.Size = new System.Drawing.Size(830, 588);
            ((System.ComponentModel.ISupportInitialize)(this.datatable)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox duzey_box;
        private System.Windows.Forms.DataGridView datatable;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button görüntüle_btn;
    }
}
