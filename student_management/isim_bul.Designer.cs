namespace student_managment
{
    partial class isim_bul
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
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle7 = new System.Windows.Forms.DataGridViewCellStyle();
            System.Windows.Forms.DataGridViewCellStyle dataGridViewCellStyle8 = new System.Windows.Forms.DataGridViewCellStyle();
            this.label1 = new System.Windows.Forms.Label();
            this.ara_btn = new System.Windows.Forms.Button();
            this.isim_entry = new System.Windows.Forms.TextBox();
            this.datatable = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.datatable)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.Location = new System.Drawing.Point(332, 7);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(153, 37);
            this.label1.TabIndex = 35;
            this.label1.Text = "İsim Ara:";
            // 
            // ara_btn
            // 
            this.ara_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.ara_btn.Location = new System.Drawing.Point(317, 139);
            this.ara_btn.Name = "ara_btn";
            this.ara_btn.Size = new System.Drawing.Size(170, 50);
            this.ara_btn.TabIndex = 34;
            this.ara_btn.Text = "İsim Ara:";
            this.ara_btn.UseVisualStyleBackColor = true;
            this.ara_btn.Click += new System.EventHandler(this.ara_btn_Click);
            // 
            // isim_entry
            // 
            this.isim_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.isim_entry.Location = new System.Drawing.Point(308, 78);
            this.isim_entry.Name = "isim_entry";
            this.isim_entry.Size = new System.Drawing.Size(193, 31);
            this.isim_entry.TabIndex = 33;
            // 
            // datatable
            // 
            dataGridViewCellStyle7.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle7.BackColor = System.Drawing.SystemColors.Control;
            dataGridViewCellStyle7.Font = new System.Drawing.Font("Microsoft Sans Serif", 21F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            dataGridViewCellStyle7.ForeColor = System.Drawing.SystemColors.WindowText;
            dataGridViewCellStyle7.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle7.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle7.WrapMode = System.Windows.Forms.DataGridViewTriState.True;
            this.datatable.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle7;
            this.datatable.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewCellStyle8.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle8.BackColor = System.Drawing.SystemColors.Window;
            dataGridViewCellStyle8.Font = new System.Drawing.Font("Microsoft Sans Serif", 21F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            dataGridViewCellStyle8.ForeColor = System.Drawing.SystemColors.ControlText;
            dataGridViewCellStyle8.SelectionBackColor = System.Drawing.SystemColors.Highlight;
            dataGridViewCellStyle8.SelectionForeColor = System.Drawing.SystemColors.HighlightText;
            dataGridViewCellStyle8.WrapMode = System.Windows.Forms.DataGridViewTriState.False;
            this.datatable.DefaultCellStyle = dataGridViewCellStyle8;
            this.datatable.Location = new System.Drawing.Point(24, 213);
            this.datatable.Name = "datatable";
            this.datatable.Size = new System.Drawing.Size(782, 336);
            this.datatable.TabIndex = 36;
            // 
            // isim_bul
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.datatable);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.ara_btn);
            this.Controls.Add(this.isim_entry);
            this.Name = "isim_bul";
            this.Size = new System.Drawing.Size(830, 588);
            ((System.ComponentModel.ISupportInitialize)(this.datatable)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button ara_btn;
        private System.Windows.Forms.TextBox isim_entry;
        private System.Windows.Forms.DataGridView datatable;
    }
}
