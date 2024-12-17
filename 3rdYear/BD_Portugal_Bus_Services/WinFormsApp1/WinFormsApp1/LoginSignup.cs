using Microsoft.Data.SqlClient;
using System;
using System.Data;
using System.Security.Cryptography;
using System.Text;
using System.Windows.Forms;

using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace WinFormsApp1
{
    public partial class LoginSignup : Form
    {
        private string conStr = Globals.strConn;
        //private string conStr = "Data Source=DESKTOP-RGVE259;Initial Catalog=EAP;Integrated Security=True;TrustServerCertificate=True";
        private menu menu;

        public LoginSignup()
        {
            InitializeComponent();
            this.menu = new menu();
        }

        private void loginButton_Click(object sender, EventArgs e)
        {
            string email = loginEmailTextBox.Text;
            string password = loginPasswordTextBox.Text;

            if (string.IsNullOrWhiteSpace(email) || string.IsNullOrWhiteSpace(password))
            {
                MessageBox.Show("Email and password cannot be empty.");
                return;
            }

            byte[] hashedPassword = ComputeSha256Hash(password);

            using (SqlConnection con = new SqlConnection(conStr))
            {
                try
                {
                    con.Open();
                    string query = "SELECT Password FROM EAP.Utilizador WHERE Email = @Email";
                    SqlCommand cmd = new SqlCommand(query, con);
                    cmd.Parameters.AddWithValue("@Email", email);
                    SqlDataReader reader = cmd.ExecuteReader();

                    if (reader.Read())
                    {
                        byte[] storedHash = (byte[])reader["Password"];
                        if (CompareHashes(storedHash, hashedPassword))
                        {
                            MessageBox.Show("Login successful!");
                            menu.Show();
                            this.Hide();
                        }
                        else
                        {
                            MessageBox.Show("Invalid email or password.");
                        }
                    }
                    else
                    {
                        MessageBox.Show("Invalid email or password.");
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error! " + ex.Message);
                }
            }
        }

        private void signupButton_Click(object sender, EventArgs e)
        {
            string email = signupEmailTextBox.Text;
            string password = signupPasswordTextBox.Text;
            string confirmPassword = confirmPasswordTextBox.Text;

            if (string.IsNullOrWhiteSpace(email) || string.IsNullOrWhiteSpace(password) || string.IsNullOrWhiteSpace(confirmPassword))
            {
                MessageBox.Show("Email and password fields cannot be empty.");
                return;
            }

            if (password != confirmPassword)
            {
                MessageBox.Show("Passwords do not match.");
                return;
            }

            byte[] hashedPassword = ComputeSha256Hash(password);

            using (SqlConnection con = new SqlConnection(conStr))
            {
                try
                {
                    con.Open();
                    string query = "INSERT INTO EAP.Utilizador (Email, Password) VALUES (@Email, @Password)";
                    SqlCommand cmd = new SqlCommand(query, con);
                    cmd.Parameters.AddWithValue("@Email", email);
                    cmd.Parameters.AddWithValue("@Password", hashedPassword);

                    int rows = cmd.ExecuteNonQuery();
                    if (rows > 0)
                    {
                        MessageBox.Show("Account created successfully!");
                        menu.Show();
                        this.Hide();
                    }
                    else
                    {
                        MessageBox.Show("Failed to create account.");
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error! " + ex.Message);
                }
            }
        }

        private static byte[] ComputeSha256Hash(string rawData)
        {
            using (SHA256 sha256Hash = SHA256.Create())
            {
                return sha256Hash.ComputeHash(Encoding.UTF8.GetBytes(rawData));
            }
        }

        private static bool CompareHashes(byte[] hash1, byte[] hash2)
        {
            if (hash1.Length != hash2.Length)
            {
                return false;
            }

            for (int i = 0; i < hash1.Length; i++)
            {
                if (hash1[i] != hash2[i])
                {
                    return false;
                }
            }

            return true;
        }

        private void loginGroupBox_Enter(object sender, EventArgs e)
        {

        }
    }
}
