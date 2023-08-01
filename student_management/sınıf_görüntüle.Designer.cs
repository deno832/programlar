namespace student_managment
{
    partial class sınıf_görüntüle
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
            this.görüntüle_btn = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.sinif_box = new System.Windows.Forms.ComboBox();
            this.datatable = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.datatable)).BeginInit();
            this.SuspendLayout();
            // 
            // görüntüle_btn
            // 
            this.görüntüle_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.görüntüle_btn.Location = new System.Drawing.Point(320, 535);
            this.görüntüle_btn.Name = "görüntüle_btn";
            this.görüntüle_btn.Size = new System.Drawing.Size(148, 53);
            this.görüntüle_btn.TabIndex = 1;
            this.görüntüle_btn.Text = "Görüntüle";
            this.görüntüle_btn.UseVisualStyleBackColor = true;
            this.görüntüle_btn.Click += new System.EventHandler(this.görüntüle_btn_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.Location = new System.Drawing.Point(273, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(252, 37);
            this.label1.TabIndex = 3;
            this.label1.Text = "Sınıfı Görüntüle";
            // 
            // sinif_box
            // 
            this.sinif_box.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.sinif_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.sinif_box.FormattingEnabled = true;
            this.sinif_box.Location = new System.Drawing.Point(344, 62);
            this.sinif_box.Name = "sinif_box";
            this.sinif_box.Size = new System.Drawing.Size(86, 37);
            this.sinif_box.TabIndex = 19;
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
            this.datatable.Location = new System.Drawing.Point(34, 124);
            this.datatable.Name = "datatable";
            this.datatable.Size = new System.Drawing.Size(763, 405);
            this.datatable.TabIndex = 20;
            // 
            // sınıf_görüntüle
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.datatable);
            this.Controls.Add(this.sinif_box);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.görüntüle_btn);
            this.Name = "sınıf_görüntüle";
            this.Size = new System.Drawing.Size(830, 588);
            this.Load += new System.EventHandler(this.sınıf_görüntüle_Load);
            ((System.ComponentModel.ISupportInitialize)(this.datatable)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button görüntüle_btn;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox sinif_box;
        private System.Windows.Forms.DataGridView datatable;
    }
}
