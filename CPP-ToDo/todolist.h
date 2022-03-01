#ifndef TODOLIST_H
#define TODOLIST_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class ToDoList; }
QT_END_NAMESPACE

class ToDoList : public QMainWindow
{
    Q_OBJECT

public:
    ToDoList(QWidget *parent = nullptr);
    ~ToDoList();

private slots:
    void on_AddTask_clicked();

    void on_DeleteTask_clicked();

private:
    Ui::ToDoList *ui;
};
#endif // TODOLIST_H
