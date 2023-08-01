namespace student_managment
{
    partial class ID_düzenle
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
            this.label3 = new System.Windows.Forms.Label();
            this.sinif_box = new System.Windows.Forms.ComboBox();
            this.save_btn = new System.Windows.Forms.Button();
            this.bolum_box = new System.Windows.Forms.ComboBox();
            this.label5 = new System.Windows.Forms.Label();
            this.soyad_entry = new System.Windows.Forms.TextBox();
            this.ad_entry = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.sil_btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label3.Location = new System.Drawing.Point(72, 205);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(196, 29);
            this.label3.TabIndex = 28;
            this.label3.Text = "Öğrencinin Sınıfı:";
            // 
            // sinif_box
            // 
            this.sinif_box.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.sinif_box.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.sinif_box.FormattingEnabled = true;
            this.sinif_box.Location = new System.Drawing.Point(285, 202);
            this.sinif_box.Name = "sinif_box";
            this.sinif_box.Size = new System.Drawing.Size(80, 32);
            this.sinif_box.TabIndex = 27;
            // 
            // save_btn
            // 
            this.save_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.save_btn.Location = new System.Drawing.Point(104, 302);
            this.save_btn.Name = "save_btn";
            this.save_btn.Size = new System.Drawing.Size(137, 44);
            this.save_btn.TabIndex = 26;
            this.save_btn.Text = "Düzenle";
            this.save_btn.UseVisualStyleBackColor = true;
            this.save_btn.Click += new System.EventHandler(this.save_btn_Click);
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
            this.bolum_box.Location = new System.Drawing.Point(309, 252);
            this.bolum_box.Name = "bolum_box";
            this.bolum_box.Size = new System.Drawing.Size(136, 28);
            this.bolum_box.TabIndex = 25;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label5.Location = new System.Drawing.Point(72, 251);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(225, 29);
            this.label5.TabIndex = 24;
            this.label5.Text = "Öğrencinin Bölümü:";
            // 
            // soyad_entry
            // 
            this.soyad_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.soyad_entry.Location = new System.Drawing.Point(295, 163);
            this.soyad_entry.Name = "soyad_entry";
            this.soyad_entry.Size = new System.Drawing.Size(185, 26);
            this.soyad_entry.TabIndex = 23;
            // 
            // ad_entry
            // 
            this.ad_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.ad_entry.Location = new System.Drawing.Point(256, 118);
            this.ad_entry.Name = "ad_entry";
            this.ad_entry.Size = new System.Drawing.Size(185, 26);
            this.ad_entry.TabIndex = 22;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label2.Location = new System.Drawing.Point(72, 159);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(217, 29);
            this.label2.TabIndex = 21;
            this.label2.Text = "Öğrencinin Soyadı:";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.Location = new System.Drawing.Point(72, 118);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(178, 29);
            this.label1.TabIndex = 20;
            this.label1.Text = "Öğrencinin Adı:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 24F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label4.Location = new System.Drawing.Point(113, 9);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(293, 37);
            this.label4.TabIndex = 29;
            this.label4.Text = "Düzenleme Ekranı";
            // 
            // sil_btn
            // 
            this.sil_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.sil_btn.Location = new System.Drawing.Point(285, 302);
            this.sil_btn.Name = "sil_btn";
            this.sil_btn.Size = new System.Drawing.Size(137, 44);
            this.sil_btn.TabIndex = 30;
            this.sil_btn.Text = "Sil";
            this.sil_btn.UseVisualStyleBackColor = true;
            this.sil_btn.Click += new System.EventHandler(this.sil_btn_Click);
            // 
            // ID_düzenle
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(534, 450);
            this.Controls.Add(this.sil_btn);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.sinif_box);
            this.Controls.Add(this.save_btn);
            this.Controls.Add(this.bolum_box);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.soyad_entry);
            this.Controls.Add(this.ad_entry);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "ID_düzenle";
            this.Text = "ID_düzenle";
            this.Load += new System.EventHandler(this.ID_düzenle_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ComboBox sinif_box;
        private System.Windows.Forms.Button save_btn;
        private System.Windows.Forms.ComboBox bolum_box;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox soyad_entry;
        private System.Windows.Forms.TextBox ad_entry;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button sil_btn;
    }
}