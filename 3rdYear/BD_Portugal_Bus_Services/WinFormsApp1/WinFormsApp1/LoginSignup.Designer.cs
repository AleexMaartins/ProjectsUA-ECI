namespace WinFormsApp1
{
    partial class LoginSignup
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
            loginGroupBox = new GroupBox();
            loginButton = new Button();
            loginPasswordTextBox = new TextBox();
            loginEmailTextBox = new TextBox();
            loginPasswordLabel = new Label();
            loginEmailLabel = new Label();
            signupGroupBox = new GroupBox();
            signupButton = new Button();
            confirmPasswordTextBox = new TextBox();
            signupPasswordTextBox = new TextBox();
            signupEmailTextBox = new TextBox();
            confirmPasswordLabel = new Label();
            signupPasswordLabel = new Label();
            signupEmailLabel = new Label();
            loginGroupBox.SuspendLayout();
            signupGroupBox.SuspendLayout();
            SuspendLayout();
            // 
            // loginGroupBox
            // 
            loginGroupBox.Controls.Add(loginButton);
            loginGroupBox.Controls.Add(loginPasswordTextBox);
            loginGroupBox.Controls.Add(loginEmailTextBox);
            loginGroupBox.Controls.Add(loginPasswordLabel);
            loginGroupBox.Controls.Add(loginEmailLabel);
            loginGroupBox.Location = new Point(12, 15);
            loginGroupBox.Margin = new Padding(3, 4, 3, 4);
            loginGroupBox.Name = "loginGroupBox";
            loginGroupBox.Padding = new Padding(3, 4, 3, 4);
            loginGroupBox.Size = new Size(300, 250);
            loginGroupBox.TabIndex = 0;
            loginGroupBox.TabStop = false;
            loginGroupBox.Text = "Login";
            loginGroupBox.Enter += loginGroupBox_Enter;
            // 
            // loginButton
            // 
            loginButton.Location = new Point(100, 188);
            loginButton.Margin = new Padding(3, 4, 3, 4);
            loginButton.Name = "loginButton";
            loginButton.Size = new Size(100, 29);
            loginButton.TabIndex = 4;
            loginButton.Text = "Login";
            loginButton.UseVisualStyleBackColor = true;
            loginButton.Click += loginButton_Click;
            // 
            // loginPasswordTextBox
            // 
            loginPasswordTextBox.Location = new Point(100, 125);
            loginPasswordTextBox.Margin = new Padding(3, 4, 3, 4);
            loginPasswordTextBox.Name = "loginPasswordTextBox";
            loginPasswordTextBox.Size = new Size(175, 27);
            loginPasswordTextBox.TabIndex = 3;
            loginPasswordTextBox.UseSystemPasswordChar = true;
            // 
            // loginEmailTextBox
            // 
            loginEmailTextBox.Location = new Point(100, 62);
            loginEmailTextBox.Margin = new Padding(3, 4, 3, 4);
            loginEmailTextBox.Name = "loginEmailTextBox";
            loginEmailTextBox.Size = new Size(175, 27);
            loginEmailTextBox.TabIndex = 2;
            // 
            // loginPasswordLabel
            // 
            loginPasswordLabel.AutoSize = true;
            loginPasswordLabel.Location = new Point(20, 125);
            loginPasswordLabel.Name = "loginPasswordLabel";
            loginPasswordLabel.Size = new Size(70, 20);
            loginPasswordLabel.TabIndex = 1;
            loginPasswordLabel.Text = "Password";
            // 
            // loginEmailLabel
            // 
            loginEmailLabel.AutoSize = true;
            loginEmailLabel.Location = new Point(20, 62);
            loginEmailLabel.Name = "loginEmailLabel";
            loginEmailLabel.Size = new Size(46, 20);
            loginEmailLabel.TabIndex = 0;
            loginEmailLabel.Text = "Email";
            // 
            // signupGroupBox
            // 
            signupGroupBox.Controls.Add(signupButton);
            signupGroupBox.Controls.Add(confirmPasswordTextBox);
            signupGroupBox.Controls.Add(signupPasswordTextBox);
            signupGroupBox.Controls.Add(signupEmailTextBox);
            signupGroupBox.Controls.Add(confirmPasswordLabel);
            signupGroupBox.Controls.Add(signupPasswordLabel);
            signupGroupBox.Controls.Add(signupEmailLabel);
            signupGroupBox.Location = new Point(330, 15);
            signupGroupBox.Margin = new Padding(3, 4, 3, 4);
            signupGroupBox.Name = "signupGroupBox";
            signupGroupBox.Padding = new Padding(3, 4, 3, 4);
            signupGroupBox.Size = new Size(300, 312);
            signupGroupBox.TabIndex = 1;
            signupGroupBox.TabStop = false;
            signupGroupBox.Text = "Signup";
            // 
            // signupButton
            // 
            signupButton.Location = new Point(100, 250);
            signupButton.Margin = new Padding(3, 4, 3, 4);
            signupButton.Name = "signupButton";
            signupButton.Size = new Size(100, 29);
            signupButton.TabIndex = 6;
            signupButton.Text = "Create Account";
            signupButton.UseVisualStyleBackColor = true;
            signupButton.Click += signupButton_Click;
            // 
            // confirmPasswordTextBox
            // 
            confirmPasswordTextBox.Location = new Point(141, 188);
            confirmPasswordTextBox.Margin = new Padding(3, 4, 3, 4);
            confirmPasswordTextBox.Name = "confirmPasswordTextBox";
            confirmPasswordTextBox.Size = new Size(153, 27);
            confirmPasswordTextBox.TabIndex = 5;
            confirmPasswordTextBox.UseSystemPasswordChar = true;
            // 
            // signupPasswordTextBox
            // 
            signupPasswordTextBox.Location = new Point(141, 125);
            signupPasswordTextBox.Margin = new Padding(3, 4, 3, 4);
            signupPasswordTextBox.Name = "signupPasswordTextBox";
            signupPasswordTextBox.Size = new Size(153, 27);
            signupPasswordTextBox.TabIndex = 4;
            signupPasswordTextBox.UseSystemPasswordChar = true;
            // 
            // signupEmailTextBox
            // 
            signupEmailTextBox.Location = new Point(141, 62);
            signupEmailTextBox.Margin = new Padding(3, 4, 3, 4);
            signupEmailTextBox.Name = "signupEmailTextBox";
            signupEmailTextBox.Size = new Size(153, 27);
            signupEmailTextBox.TabIndex = 3;
            // 
            // confirmPasswordLabel
            // 
            confirmPasswordLabel.AutoSize = true;
            confirmPasswordLabel.Location = new Point(10, 188);
            confirmPasswordLabel.Name = "confirmPasswordLabel";
            confirmPasswordLabel.Size = new Size(127, 20);
            confirmPasswordLabel.TabIndex = 2;
            confirmPasswordLabel.Text = "Confirm Password";
            // 
            // signupPasswordLabel
            // 
            signupPasswordLabel.AutoSize = true;
            signupPasswordLabel.Location = new Point(10, 125);
            signupPasswordLabel.Name = "signupPasswordLabel";
            signupPasswordLabel.Size = new Size(70, 20);
            signupPasswordLabel.TabIndex = 1;
            signupPasswordLabel.Text = "Password";
            // 
            // signupEmailLabel
            // 
            signupEmailLabel.AutoSize = true;
            signupEmailLabel.Location = new Point(10, 62);
            signupEmailLabel.Name = "signupEmailLabel";
            signupEmailLabel.Size = new Size(46, 20);
            signupEmailLabel.TabIndex = 0;
            signupEmailLabel.Text = "Email";
            // 
            // LoginSignup
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(650, 350);
            Controls.Add(signupGroupBox);
            Controls.Add(loginGroupBox);
            Margin = new Padding(3, 4, 3, 4);
            Name = "LoginSignup";
            Text = "Login and Signup";
            loginGroupBox.ResumeLayout(false);
            loginGroupBox.PerformLayout();
            signupGroupBox.ResumeLayout(false);
            signupGroupBox.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private System.Windows.Forms.GroupBox loginGroupBox;
        private System.Windows.Forms.Button loginButton;
        private System.Windows.Forms.TextBox loginPasswordTextBox;
        private System.Windows.Forms.TextBox loginEmailTextBox;
        private System.Windows.Forms.Label loginPasswordLabel;
        private System.Windows.Forms.Label loginEmailLabel;
        private System.Windows.Forms.GroupBox signupGroupBox;
        private System.Windows.Forms.Button signupButton;
        private System.Windows.Forms.TextBox confirmPasswordTextBox;
        private System.Windows.Forms.TextBox signupPasswordTextBox;
        private System.Windows.Forms.TextBox signupEmailTextBox;
        private System.Windows.Forms.Label confirmPasswordLabel;
        private System.Windows.Forms.Label signupPasswordLabel;
        private System.Windows.Forms.Label signupEmailLabel;
    }
}
