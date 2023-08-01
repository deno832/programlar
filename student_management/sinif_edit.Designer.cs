namespace student_managment
{
    partial class sinif_edit
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
            this.panel1 = new System.Windows.Forms.Panel();
            this.delete_btn = new System.Windows.Forms.Button();
            this.duzey_box = new System.Windows.Forms.ComboBox();
            this.bolum_box = new System.Windows.Forms.ComboBox();
            this.edit_btn = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.şube_entry = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.panel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.panel1.Controls.Add(this.delete_btn);
            this.panel1.Controls.Add(this.duzey_box);
            this.panel1.Controls.Add(this.bolum_box);
            this.panel1.Controls.Add(this.edit_btn);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.şube_entry);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Location = new System.Drawing.Point(12, 26);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(408, 369);
            this.panel1.TabIndex = 10;
            // 
            // delete_btn
            // 
            this.delete_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.delete_btn.Location = new System.Drawing.Point(231, 236);
            this.delete_btn.Name = "delete_btn";
            this.delete_btn.Size = new System.Drawing.Size(128, 45);
            this.delete_btn.TabIndex = 15;
            this.delete_btn.Text = "Sınıfı Sil";
            this.delete_btn.UseVisualStyleBackColor = true;
            this.delete_btn.Click += new System.EventHandler(this.delete_btn_Click);
            // 
            // duzey_box
            // 
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
            this.duzey_box.Location = new System.Drawing.Point(199, 106);
            this.duzey_box.Name = "duzey_box";
            this.duzey_box.Size = new System.Drawing.Size(80, 32);
            this.duzey_box.TabIndex = 14;
            // 
            // bolum_box
            // 
            this.bolum_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.bolum_box.FormattingEnabled = true;
            this.bolum_box.Items.AddRange(new object[] {
            "İlk Okul",
            "Orta Okul",
            "Lise"});
            this.bolum_box.Location = new System.Drawing.Point(198, 67);
            this.bolum_box.Name = "bolum_box";
            this.bolum_box.Size = new System.Drawing.Size(136, 28);
            this.bolum_box.TabIndex = 13;
            // 
            // edit_btn
            // 
            this.edit_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.edit_btn.Location = new System.Drawing.Point(49, 236);
            this.edit_btn.Name = "edit_btn";
            this.edit_btn.Size = new System.Drawing.Size(128, 45);
            this.edit_btn.TabIndex = 11;
            this.edit_btn.Text = "Düzenle";
            this.edit_btn.UseVisualStyleBackColor = true;
            this.edit_btn.Click += new System.EventHandler(this.edit_btn_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 21.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label5.Location = new System.Drawing.Point(110, 2);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(208, 33);
            this.label5.TabIndex = 10;
            this.label5.Text = "Sınıfı Düzenle";
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
            // şube_entry
            // 
            this.şube_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.şube_entry.Location = new System.Drawing.Point(198, 155);
            this.şube_entry.Name = "şube_entry";
            this.şube_entry.Size = new System.Drawing.Size(173, 29);
            this.şube_entry.TabIndex = 8;
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
            // sinif_edit
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(448, 424);
            this.Controls.Add(this.panel1);
            this.Name = "sinif_edit";
            this.Text = "sinif_edit";
            this.Load += new System.EventHandler(this.sinif_edit_Load);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.ComboBox bolum_box;
        private System.Windows.Forms.Button edit_btn;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox şube_entry;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ComboBox duzey_box;
        private System.Windows.Forms.Button delete_btn;
    }
}