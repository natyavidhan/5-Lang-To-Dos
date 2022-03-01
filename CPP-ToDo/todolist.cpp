#include "todolist.h"
#include "ui_todolist.h"

ToDoList::ToDoList(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::ToDoList)
{
    ui->setupUi(this);
}

ToDoList::~ToDoList()
{
    delete ui;
}


void ToDoList::on_AddTask_clicked()
{
    //add the text from the line edit to the list
    ui->TaskList->addItem(ui->TaskInput->text());
    //clear the line edit
    ui->TaskInput->clear();
}


void ToDoList::on_DeleteTask_clicked()
{
    //delete the selected item from the list
    ui->TaskList->takeItem(ui->TaskList->currentRow());

}

