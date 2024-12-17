using Microsoft.Data.SqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormsApp1
{
    public partial class ShowAutocarro : Form
    {
        //private string conStr = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";
        private string conStr = Globals.strConn;
        private menu menu;
        private AddAutocarros addAutocarros;

        public ShowAutocarro(menu menu)
        {
            InitializeComponent();
            displayAutocarros();
            addAutocarros = new AddAutocarros(this);
            this.menu = menu;
        }

        private void ShowAutocarro_Load(object sender, EventArgs e)
        {

        }
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
        public void displayAutocarros()
        {
            using (SqlConnection con = new SqlConnection(conStr))
            {
                try
                {
                    con.Open();
                    string query = "SELECT * FROM EAP.Autocarro";
                    SqlDataAdapter da = new SqlDataAdapter(query, con);
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    dataGridView1.DataSource = dt;

                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error! " + ex.Message);
                }
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            addAutocarros.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            menu.Show();
            this.Hide();
        }
    }
}