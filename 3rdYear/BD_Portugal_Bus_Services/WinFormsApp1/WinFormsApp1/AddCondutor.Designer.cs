namespace WinFormsApp1
{
    partial class AddCondutor
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
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            textBox4 = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            textBox5 = new TextBox();
            textBox1 = new TextBox();
            button1 = new Button();
            button2 = new Button();
            SuspendLayout();
            // 
            // textBox2
            // 
            textBox2.Location = new Point(150, 102);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(461, 27);
            textBox2.TabIndex = 1;
            textBox2.TextChanged += textBox2_TextChanged;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(150, 156);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(461, 27);
            textBox3.TabIndex = 2;
            textBox3.TextChanged += textBox3_TextChanged;
            // 
            // textBox4
            // 
            textBox4.Location = new Point(150, 211);
            textBox4.Name = "textBox4";
            textBox4.Size = new Size(461, 27);
            textBox4.TabIndex = 3;
            textBox4.TextChanged += textBox4_TextChanged;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(354, 22);
            label1.Name = "label1";
            label1.Size = new Size(47, 20);
            label1.TabIndex = 5;
            label1.Text = "nome";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(346, 79);
            label2.Name = "label2";
            label2.Size = new Size(60, 20);
            label2.TabIndex = 6;
            label2.Text = "apelido";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(351, 133);
            label3.Name = "label3";
            label3.Size = new Size(46, 20);
            label3.TabIndex = 7;
            label3.Text = "email";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(363, 188);
            label4.Name = "label4";
            label4.Size = new Size(26, 20);
            label4.TabIndex = 8;
            label4.Text = "nif";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(313, 250);
            label5.Name = "label5";
            label5.Size = new Size(132, 20);
            label5.TabIndex = 10;
            label5.Text = "carta de condução";
            label5.Click += label5_Click;
            // 
            // textBox5
            // 
            textBox5.Location = new Point(150, 273);
            textBox5.Name = "textBox5";
            textBox5.Size = new Size(461, 27);
            textBox5.TabIndex = 9;
            textBox5.TextChanged += textBox5_TextChanged;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(150, 45);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(461, 27);
            textBox1.TabIndex = 0;
            textBox1.TextChanged += textBox1_TextChanged;
            // 
            // button1
            // 
            button1.Location = new Point(267, 315);
            button1.Name = "button1";
            button1.Size = new Size(240, 29);
            button1.TabIndex = 13;
            button1.Text = "Adicionar Condutor";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(12, 22);
            button2.Name = "button2";
            button2.Size = new Size(63, 40);
            button2.TabIndex = 14;
            button2.Text = "Voltar";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // AddCondutor
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(button2);
            Controls.Add(button1);
            Controls.Add(label5);
            Controls.Add(textBox5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(textBox4);
            Controls.Add(textBox3);
            Controls.Add(textBox2);
            Controls.Add(textBox1);
            Name = "AddCondutor";
            Text = "Form1";
            Load += AddCondutor_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion
        private TextBox textBox2;
        private TextBox textBox3;
        private TextBox textBox4;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private TextBox textBox5;
        private TextBox textBox1;
        private Button button1;
        private Button button2;
    }
}