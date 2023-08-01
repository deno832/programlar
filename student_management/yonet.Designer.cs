namespace student_managment
{
    partial class yonet
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
            this.label1 = new System.Windows.Forms.Label();
            this.sınıflar_panel = new System.Windows.Forms.FlowLayoutPanel();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.şube_entry = new System.Windows.Forms.TextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.bolum_box = new System.Windows.Forms.ComboBox();
            this.duzey_box = new System.Windows.Forms.ComboBox();
            this.add_btn = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 26.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.Location = new System.Drawing.Point(264, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(246, 39);
            this.label1.TabIndex = 0;
            this.label1.Text = "Sınıfları Yönet";
            // 
            // sınıflar_panel
            // 
            this.sınıflar_panel.AutoScroll = true;
            this.sınıflar_panel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.sınıflar_panel.FlowDirection = System.Windows.Forms.FlowDirection.TopDown;
            this.sınıflar_panel.Location = new System.Drawing.Point(29, 110);
            this.sınıflar_panel.Name = "sınıflar_panel";
            this.sınıflar_panel.Padding = new System.Windows.Forms.Padding(10, 5, 0, 0);
            this.sınıflar_panel.Size = new System.Drawing.Size(263, 438);
            this.sınıflar_panel.TabIndex = 1;
            this.sınıflar_panel.WrapContents = false;
            this.sınıflar_panel.Paint += new System.Windows.Forms.PaintEventHandler(this.sınıflar_panel_Paint);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label3.Location = new System.Drawing.Point(27, 107);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(166, 31);
            this.label3.TabIndex = 3;
            this.label3.Text = "Sınıf Düzeyi:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label2.Location = new System.Drawing.Point(27, 62);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(98, 31);
            this.label2.TabIndex = 4;
            this.label2.Text = "Bölüm:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label4.Location = new System.Drawing.Point(27, 151);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(85, 31);
            this.label4.TabIndex = 5;
            this.label4.Text = "Şube:";
            // 
            // şube_entry
            // 
            this.şube_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.şube_entry.Location = new System.Drawing.Point(198, 155);
            this.şube_entry.Name = "şube_entry";
            this.şube_entry.Size = new System.Drawing.Size(173, 29);
            this.şube_entry.TabIndex = 8;
            // 
            // panel1
            // 
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel1.Controls.Add(this.bolum_box);
            this.panel1.Controls.Add(this.duzey_box);
            this.panel1.Controls.Add(this.add_btn);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.şube_entry);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Location = new System.Drawing.Point(361, 129);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(408, 369);
            this.panel1.TabIndex = 9;
            this.panel1.Paint += new System.Windows.Forms.PaintEventHandler(this.panel1_Paint);
            // 
            // bolum_box
            // 
            this.bolum_box.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.bolum_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.bolum_box.FormattingEnabled = true;
            this.bolum_box.Items.AddRange(new object[] {
            "İlk Okul",
            "Orta Okul",
            "Lise"});
            this.bolum_box.Location = new System.Drawing.Point(198, 66);
            this.bolum_box.Name = "bolum_box";
            this.bolum_box.Size = new System.Drawing.Size(136, 28);
            this.bolum_box.TabIndex = 13;
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
            this.duzey_box.Location = new System.Drawing.Point(199, 108);
            this.duzey_box.Name = "duzey_box";
            this.duzey_box.Size = new System.Drawing.Size(80, 32);
            this.duzey_box.TabIndex = 12;
            // 
            // add_btn
            // 
            this.add_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.add_btn.Location = new System.Drawing.Point(147, 236);
            this.add_btn.Name = "add_btn";
            this.add_btn.Size = new System.Drawing.Size(128, 45);
            this.add_btn.TabIndex = 11;
            this.add_btn.Text = "Ekle";
            this.add_btn.UseVisualStyleBackColor = true;
            this.add_btn.Click += new System.EventHandler(this.add_btn_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label5.Location = new System.Drawing.Point(128, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(147, 33);
            this.label5.TabIndex = 10;
            this.label5.Text = "Sınıf Ekle";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label6.Location = new System.Drawing.Point(100, 73);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(113, 33);
            this.label6.TabIndex = 14;
            this.label6.Text = "Sınıflar";
            // 
            // yonet
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.label6);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.sınıflar_panel);
            this.Controls.Add(this.label1);
            this.Name = "yonet";
            this.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.Size = new System.Drawing.Size(830, 588);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.FlowLayoutPanel sınıflar_panel;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox şube_entry;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Button add_btn;
        private System.Windows.Forms.ComboBox duzey_box;
        private System.Windows.Forms.ComboBox bolum_box;
        private System.Windows.Forms.Label label6;
    }
}
