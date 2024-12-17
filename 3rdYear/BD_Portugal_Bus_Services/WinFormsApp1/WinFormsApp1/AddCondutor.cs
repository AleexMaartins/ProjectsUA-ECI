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
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WinFormsApp1
{
    public partial class AddCondutor : Form
    {
        private ShowPeople showPeople;
        //private string conStr = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";
        private string conStr = Globals.strConn;

        public AddCondutor(ShowPeople showPeople)
        {
            InitializeComponent();
            this.showPeople = showPeople;
        }
        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }
        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (int.TryParse(textBox4.Text, out int NIF))
            {
                string nome = textBox1.Text;
                string apelido = textBox2.Text;
                string email = textBox3.Text;
                string nif = textBox4.Text;
                string carta_conducao = textBox5.Text;

                using (SqlConnection con = new SqlConnection(conStr))
                {
                    try
                    {
                        con.Open();
                        string query = "EXEC EAP.addCondutor @nome, @apelido, @email, @nif, @carta_conducao";

                        using (SqlCommand cmd = new SqlCommand(query, con))
                        {
                            cmd.Parameters.AddWithValue("@nome", nome);
                            cmd.Parameters.AddWithValue("@apelido", apelido);
                            cmd.Parameters.AddWithValue("@email", email);
                            cmd.Parameters.AddWithValue("@nif", nif);
                            cmd.Parameters.AddWithValue("@carta_conducao", carta_conducao);
                            cmd.ExecuteNonQuery();
                        }

                        MessageBox.Show("Condutor adicionado com sucesso!");

                        showPeople.displayPessoas();

                        this.Hide();
                        showPeople.Show();
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("Error! " + ex.Message);
                    }
                }
            }
            else
            {
                MessageBox.Show("Dados inseridos inválidos");
            }
        }

        private void AddCondutor_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            showPeople.displayPessoas();
            this.Hide();
            showPeople.Show();
        }
    }
}
