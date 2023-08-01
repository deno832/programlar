namespace ilk_sqlite_console
{
    partial class edit_ucontrol
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
            this.baslik_entry = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.not_entry = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.save_btn = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.del_btn = new System.Windows.Forms.Button();
            this.exit_btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // baslik_entry
            // 
            this.baslik_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.baslik_entry.Location = new System.Drawing.Point(163, 17);
            this.baslik_entry.Name = "baslik_entry";
            this.baslik_entry.Size = new System.Drawing.Size(400, 31);
            this.baslik_entry.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.Location = new System.Drawing.Point(11, 17);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(148, 29);
            this.label1.TabIndex = 1;
            this.label1.Text = "Not Başlığı:";
            // 
            // not_entry
            // 
            this.not_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.not_entry.Location = new System.Drawing.Point(16, 86);
            this.not_entry.Multiline = true;
            this.not_entry.Name = "not_entry";
            this.not_entry.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.not_entry.Size = new System.Drawing.Size(547, 511);
            this.not_entry.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label2.Location = new System.Drawing.Point(11, 50);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(61, 29);
            this.label2.TabIndex = 3;
            this.label2.Text = "Not:";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // save_btn
            // 
            this.save_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.save_btn.Location = new System.Drawing.Point(26, 603);
            this.save_btn.Name = "save_btn";
            this.save_btn.Size = new System.Drawing.Size(225, 43);
            this.save_btn.TabIndex = 4;
            this.save_btn.Text = "Değişiklikleri Kaydet";
            this.save_btn.UseVisualStyleBackColor = true;
            this.save_btn.Click += new System.EventHandler(this.save_btn_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(338, 684);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(16, 8);
            this.button1.TabIndex = 5;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // del_btn
            // 
            this.del_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.del_btn.Location = new System.Drawing.Point(257, 603);
            this.del_btn.Name = "del_btn";
            this.del_btn.Size = new System.Drawing.Size(143, 43);
            this.del_btn.TabIndex = 6;
            this.del_btn.Text = "Notu Sil";
            this.del_btn.UseVisualStyleBackColor = true;
            this.del_btn.Click += new System.EventHandler(this.del_btn_Click);
            // 
            // exit_btn
            // 
            this.exit_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.exit_btn.Location = new System.Drawing.Point(406, 603);
            this.exit_btn.Name = "exit_btn";
            this.exit_btn.Size = new System.Drawing.Size(143, 43);
            this.exit_btn.TabIndex = 7;
            this.exit_btn.Text = "Çık";
            this.exit_btn.UseVisualStyleBackColor = true;
            this.exit_btn.Click += new System.EventHandler(this.button2_Click);
            // 
            // edit_ucontrol
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.exit_btn);
            this.Controls.Add(this.del_btn);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.save_btn);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.not_entry);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.baslik_entry);
            this.Name = "edit_ucontrol";
            this.Size = new System.Drawing.Size(583, 660);
            this.Load += new System.EventHandler(this.edit_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox baslik_entry;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox not_entry;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button save_btn;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button del_btn;
        private System.Windows.Forms.Button exit_btn;
    }
}
