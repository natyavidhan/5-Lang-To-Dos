using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace C_Sharp_ToDo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //take text from input and add to listbox
            listBox1.Items.Add(textBox1.Text);
            textBox1.Text = "";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //remove selected item from listbox
            listBox1.Items.Remove(listBox1.SelectedItem);
        }
    }
}
