namespace student_managment
{
    partial class Form1
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
            this.controls_panel = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.s = new System.Windows.Forms.Button();
            this.düzey_bul = new System.Windows.Forms.Button();
            this.sınıf_görüntüle_btn = new System.Windows.Forms.Button();
            this.sinif_yonet = new System.Windows.Forms.Button();
            this.view_btn = new System.Windows.Forms.Button();
            this.kayit_controls = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.panel2.SuspendLayout();
            this.SuspendLayout();
            // 
            // controls_panel
            // 
            this.controls_panel.Location = new System.Drawing.Point(196, 12);
            this.controls_panel.Name = "controls_panel";
            this.controls_panel.Size = new System.Drawing.Size(830, 588);
            this.controls_panel.TabIndex = 0;
            this.controls_panel.Paint += new System.Windows.Forms.PaintEventHandler(this.controls_panel_Paint);
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.SystemColors.MenuHighlight;
            this.panel2.Controls.Add(this.button1);
            this.panel2.Controls.Add(this.s);
            this.panel2.Controls.Add(this.düzey_bul);
            this.panel2.Controls.Add(this.sınıf_görüntüle_btn);
            this.panel2.Controls.Add(this.sinif_yonet);
            this.panel2.Controls.Add(this.view_btn);
            this.panel2.Controls.Add(this.kayit_controls);
            this.panel2.Location = new System.Drawing.Point(12, 12);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(170, 588);
            this.panel2.TabIndex = 1;
            // 
            // s
            // 
            this.s.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.s.Location = new System.Drawing.Point(8, 387);
            this.s.Name = "s";
            this.s.Size = new System.Drawing.Size(148, 65);
            this.s.TabIndex = 7;
            this.s.Text = "ID ile Öğrenci Bul";
            this.s.UseVisualStyleBackColor = true;
            this.s.Click += new System.EventHandler(this.s_Click);
            // 
            // düzey_bul
            // 
            this.düzey_bul.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.düzey_bul.Location = new System.Drawing.Point(8, 295);
            this.düzey_bul.Name = "düzey_bul";
            this.düzey_bul.Size = new System.Drawing.Size(148, 85);
            this.düzey_bul.TabIndex = 6;
            this.düzey_bul.Text = "Sınıf Düzeyini Listele";
            this.düzey_bul.UseVisualStyleBackColor = true;
            this.düzey_bul.Click += new System.EventHandler(this.düzey_bul_Click);
            // 
            // sınıf_görüntüle_btn
            // 
            this.sınıf_görüntüle_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.sınıf_görüntüle_btn.Location = new System.Drawing.Point(8, 153);
            this.sınıf_görüntüle_btn.Name = "sınıf_görüntüle_btn";
            this.sınıf_görüntüle_btn.Size = new System.Drawing.Size(148, 62);
            this.sınıf_görüntüle_btn.TabIndex = 4;
            this.sınıf_görüntüle_btn.Text = "Sınıfları Görüntüle";
            this.sınıf_görüntüle_btn.UseVisualStyleBackColor = true;
            this.sınıf_görüntüle_btn.Click += new System.EventHandler(this.sınıf_görüntüle_btn_Click);
            // 
            // sinif_yonet
            // 
            this.sinif_yonet.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.sinif_yonet.Location = new System.Drawing.Point(8, 224);
            this.sinif_yonet.Name = "sinif_yonet";
            this.sinif_yonet.Size = new System.Drawing.Size(148, 62);
            this.sinif_yonet.TabIndex = 3;
            this.sinif_yonet.Text = "Sınıfları Yönet";
            this.sinif_yonet.UseVisualStyleBackColor = true;
            this.sinif_yonet.Click += new System.EventHandler(this.sinif_yonet_Click);
            // 
            // view_btn
            // 
            this.view_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.view_btn.Location = new System.Drawing.Point(8, 83);
            this.view_btn.Name = "view_btn";
            this.view_btn.Size = new System.Drawing.Size(148, 62);
            this.view_btn.TabIndex = 1;
            this.view_btn.Text = "Veriyi Görüntüle";
            this.view_btn.UseVisualStyleBackColor = true;
            this.view_btn.Click += new System.EventHandler(this.view_btn_Click);
            // 
            // kayit_controls
            // 
            this.kayit_controls.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.kayit_controls.Location = new System.Drawing.Point(8, 25);
            this.kayit_controls.Name = "kayit_controls";
            this.kayit_controls.Size = new System.Drawing.Size(148, 53);
            this.kayit_controls.TabIndex = 0;
            this.kayit_controls.Text = "Yeni Kayıt";
            this.kayit_controls.UseVisualStyleBackColor = true;
            this.kayit_controls.Click += new System.EventHandler(this.kayit_controls_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.button1.Location = new System.Drawing.Point(8, 458);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(148, 65);
            this.button1.TabIndex = 8;
            this.button1.Text = "İsim ile Öğrenci Ara";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click_1);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1040, 612);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.controls_panel);
            this.Name = "Form1";
            this.Text = "Öğrenci Yönetim Sistemi";
            this.panel2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel controls_panel;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Button kayit_controls;
        private System.Windows.Forms.Button view_btn;
        private System.Windows.Forms.Button sinif_yonet;
        private System.Windows.Forms.Button sınıf_görüntüle_btn;
        private System.Windows.Forms.Button düzey_bul;
        private System.Windows.Forms.Button s;
        private System.Windows.Forms.Button button1;
    }
}

