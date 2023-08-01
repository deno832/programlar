using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace student_managment
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            controls_panel.Controls.Add(new yonet());
        }

        private void controls_panel_Paint(object sender, PaintEventArgs e)
        {
            
        }

        private void kayit_controls_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            kayit controls = new kayit();
            controls_panel.Controls.Add(controls);
        }

        private void sinif_yonet_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            yonet controls = new yonet();
            controls_panel.Controls.Add(controls);
        }

        private void view_btn_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            görüntüle controls = new görüntüle();
            controls_panel.Controls.Add(controls);
        }

        private void filter_btn_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            görüntüle controls = new görüntüle();
            controls_panel.Controls.Add(controls);
        }

        private void sınıf_görüntüle_btn_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            sınıf_görüntüle controls = new sınıf_görüntüle();
            controls_panel.Controls.Add(controls);
        }

        private void düzey_bul_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            duzey_bul_cont controls = new duzey_bul_cont();
            controls_panel.Controls.Add(controls);
        }

        private void s_Click(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            id_bul controls = new id_bul();
            controls_panel.Controls.Add(controls);
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            controls_panel.Controls.Clear();
            isim_bul controls = new isim_bul();
            controls_panel.Controls.Add(controls);
        }
    }
}
