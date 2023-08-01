namespace ilk_sqlite_console
{
    partial class @new
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
            this.exit_btn = new System.Windows.Forms.Button();
            this.save_btn = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.not_entry = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.baslik_entry = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // exit_btn
            // 
            this.exit_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.exit_btn.Location = new System.Drawing.Point(348, 602);
            this.exit_btn.Name = "exit_btn";
            this.exit_btn.Size = new System.Drawing.Size(143, 43);
            this.exit_btn.TabIndex = 14;
            this.exit_btn.Text = "Çık";
            this.exit_btn.UseVisualStyleBackColor = true;
            this.exit_btn.Click += new System.EventHandler(this.exit_btn_Click);
            // 
            // save_btn
            // 
            this.save_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.save_btn.Location = new System.Drawing.Point(76, 602);
            this.save_btn.Name = "save_btn";
            this.save_btn.Size = new System.Drawing.Size(225, 43);
            this.save_btn.TabIndex = 12;
            this.save_btn.Text = "Not Oluştur";
            this.save_btn.UseVisualStyleBackColor = true;
            this.save_btn.Click += new System.EventHandler(this.save_btn_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label2.Location = new System.Drawing.Point(15, 49);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(61, 29);
            this.label2.TabIndex = 11;
            this.label2.Text = "Not:";
            // 
            // not_entry
            // 
            this.not_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.not_entry.Location = new System.Drawing.Point(20, 85);
            this.not_entry.Multiline = true;
            this.not_entry.Name = "not_entry";
            this.not_entry.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.not_entry.Size = new System.Drawing.Size(547, 511);
            this.not_entry.TabIndex = 10;
            this.not_entry.TextChanged += new System.EventHandler(this.not_entry_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.Location = new System.Drawing.Point(15, 16);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(148, 29);
            this.label1.TabIndex = 9;
            this.label1.Text = "Not Başlığı:";
            // 
            // baslik_entry
            // 
            this.baslik_entry.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.baslik_entry.Location = new System.Drawing.Point(167, 16);
            this.baslik_entry.Name = "baslik_entry";
            this.baslik_entry.Size = new System.Drawing.Size(400, 31);
            this.baslik_entry.TabIndex = 8;
            // 
            // @new
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.exit_btn);
            this.Controls.Add(this.save_btn);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.not_entry);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.baslik_entry);
            this.Name = "@new";
            this.Size = new System.Drawing.Size(583, 660);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button exit_btn;
        private System.Windows.Forms.Button save_btn;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox not_entry;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox baslik_entry;
    }
}
