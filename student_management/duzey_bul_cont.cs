using Npgsql;
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
    public partial class duzey_bul_cont : UserControl
    {
        public duzey_bul_cont()
        {
            InitializeComponent();
        }

        private void görüntüle_btn_Click(object sender, EventArgs e)
        {
            string connectionString = "Host=localhost;Port=54321;Database=okul_yönetimi;Username=postgres;Password=2008deno";
            
            string sınıf_düzeyi = duzey_box.SelectedItem?.ToString(); ;
            


            string sql = $"SELECT * FROM öğrenciler WHERE sınıf_düzeyi = '{sınıf_düzeyi}'";
            using (NpgsqlDataAdapter adapter = new NpgsqlDataAdapter(sql, connectionString))
            {
                DataSet dataSet = new DataSet();

                // Verileri DataSet'e yükleyin
                adapter.Fill(dataSet);

                // DataGridView'e DataSet'teki verileri bağlayın
                datatable.DataSource = dataSet.Tables[0];
            }
        }
    }
}
