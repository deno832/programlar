namespace ilk_sqlite_console
{
    partial class Form1
    {
        /// <summary>
        ///Gerekli tasarımcı değişkeni.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///Kullanılan tüm kaynakları temizleyin.
        /// </summary>
        ///<param name="disposing">yönetilen kaynaklar dispose edilmeliyse doğru; aksi halde yanlış.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer üretilen kod

        /// <summary>
        /// Tasarımcı desteği için gerekli metot - bu metodun 
        ///içeriğini kod düzenleyici ile değiştirmeyin.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.NotePanel = new System.Windows.Forms.FlowLayoutPanel();
            this.create_btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 20.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.label1.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.label1.Location = new System.Drawing.Point(49, 14);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(317, 31);
            this.label1.TabIndex = 0;
            this.label1.Text = "Kıytırık Not Uygulaması";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // NotePanel
            // 
            this.NotePanel.AutoScroll = true;
            this.NotePanel.FlowDirection = System.Windows.Forms.FlowDirection.TopDown;
            this.NotePanel.Location = new System.Drawing.Point(12, 65);
            this.NotePanel.Name = "NotePanel";
            this.NotePanel.Padding = new System.Windows.Forms.Padding(10, 5, 0, 0);
            this.NotePanel.Size = new System.Drawing.Size(400, 469);
            this.NotePanel.TabIndex = 1;
            this.NotePanel.WrapContents = false;
            this.NotePanel.Paint += new System.Windows.Forms.PaintEventHandler(this.flowLayoutPanel1_Paint);
            // 
            // create_btn
            // 
            this.create_btn.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(162)));
            this.create_btn.Location = new System.Drawing.Point(101, 551);
            this.create_btn.Name = "create_btn";
            this.create_btn.Size = new System.Drawing.Size(213, 43);
            this.create_btn.TabIndex = 7;
            this.create_btn.Text = "Yeni Not Oluştur";
            this.create_btn.UseVisualStyleBackColor = true;
            this.create_btn.Click += new System.EventHandler(this.del_btn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(424, 611);
            this.Controls.Add(this.create_btn);
            this.Controls.Add(this.NotePanel);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.FlowLayoutPanel NotePanel;
        private System.Windows.Forms.Button create_btn;
    }
}

