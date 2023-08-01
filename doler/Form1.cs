using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace doler
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            Thread thread = new Thread(ThreadMethod);
            thread.Start();
            InitializeComponent();
        }
        public async void ThreadMethod()
        {
            while(true) {
                System.Threading.Thread.Sleep(5000);
                HttpClient client = new HttpClient();

                try
                {
                    // Talebi gönder
                    HttpResponseMessage response = await client.GetAsync("https://api.genelpara.com/embed/para-birimleri.json");

                    // Yanıtı oku
                    string responseBody = await response.Content.ReadAsStringAsync();

                    JObject jsonData = JObject.Parse(responseBody);
                    JToken usd = jsonData["USD"];
                    string dolar_deger = (string)usd["satis"];

                    JToken euro = jsonData["EUR"];
                    string euro_deger = (string)euro["satis"];

                    this.Invoke((MethodInvoker)delegate ()
                    {
                        dolar_lbl.Text = dolar_deger;
                        euro_lbl.Text = euro_deger;
                    });

                }
                catch (HttpRequestException ex)
                {
                    // Hata durumunda işle
                    Console.WriteLine($"Hata: {ex.Message}");
                }
                finally
                {
                    // HttpClient'i temizle
                    client.Dispose();
                }
            }
        }
        
        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void dolar_Click(object sender, EventArgs e)
        {

        }
    }
}
