/********************************************************************************
** Form generated from reading UI file 'pong.ui'
**
** Created by: Qt User Interface Compiler version 5.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_PONG_H
#define UI_PONG_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QSplitter>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Pong
{
public:
    QLabel *label_5;
    QLabel *label_6;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QWidget *layoutWidget1;
    QHBoxLayout *horizontalLayout_6;
    QHBoxLayout *horizontalLayout_4;
    QSplitter *splitter;
    QLabel *label;
    QLineEdit *lineEdit;
    QSpacerItem *horizontalSpacer;
    QHBoxLayout *horizontalLayout_5;
    QRadioButton *radioButton;
    QRadioButton *radioButton_2;
    QSpacerItem *horizontalSpacer_2;
    QPushButton *pushButton;

    void setupUi(QWidget *Pong)
    {
        if (Pong->objectName().isEmpty())
            Pong->setObjectName(QStringLiteral("Pong"));
        Pong->resize(570, 262);
        Pong->setAutoFillBackground(false);
        label_5 = new QLabel(Pong);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(230, 10, 121, 41));
        label_6 = new QLabel(Pong);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(110, 210, 351, 31));
        layoutWidget = new QWidget(Pong);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(190, 60, 201, 87));
        horizontalLayout_2 = new QHBoxLayout(layoutWidget);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        label_2 = new QLabel(layoutWidget);
        label_2->setObjectName(QStringLiteral("label_2"));

        horizontalLayout_2->addWidget(label_2);

        label_3 = new QLabel(layoutWidget);
        label_3->setObjectName(QStringLiteral("label_3"));

        horizontalLayout_2->addWidget(label_3);

        label_4 = new QLabel(layoutWidget);
        label_4->setObjectName(QStringLiteral("label_4"));

        horizontalLayout_2->addWidget(label_4);

        layoutWidget1 = new QWidget(Pong);
        layoutWidget1->setObjectName(QStringLiteral("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(20, 170, 541, 35));
        horizontalLayout_6 = new QHBoxLayout(layoutWidget1);
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        horizontalLayout_6->setContentsMargins(0, 0, 0, 0);
        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        splitter = new QSplitter(layoutWidget1);
        splitter->setObjectName(QStringLiteral("splitter"));
        splitter->setOrientation(Qt::Horizontal);
        label = new QLabel(splitter);
        label->setObjectName(QStringLiteral("label"));
        splitter->addWidget(label);
        lineEdit = new QLineEdit(splitter);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        splitter->addWidget(lineEdit);

        horizontalLayout_4->addWidget(splitter);


        horizontalLayout_6->addLayout(horizontalLayout_4);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer);

        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        radioButton = new QRadioButton(layoutWidget1);
        radioButton->setObjectName(QStringLiteral("radioButton"));

        horizontalLayout_5->addWidget(radioButton);

        radioButton_2 = new QRadioButton(layoutWidget1);
        radioButton_2->setObjectName(QStringLiteral("radioButton_2"));

        horizontalLayout_5->addWidget(radioButton_2);


        horizontalLayout_6->addLayout(horizontalLayout_5);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_6->addItem(horizontalSpacer_2);

        pushButton = new QPushButton(layoutWidget1);
        pushButton->setObjectName(QStringLiteral("pushButton"));

        horizontalLayout_6->addWidget(pushButton);

        layoutWidget->raise();
        layoutWidget->raise();
        label_5->raise();
        label_6->raise();

        retranslateUi(Pong);

        QMetaObject::connectSlotsByName(Pong);
    } // setupUi

    void retranslateUi(QWidget *Pong)
    {
        Pong->setWindowTitle(QApplication::translate("Pong", "Pong", 0));
        label_5->setText(QApplication::translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Placar</span></p></body></html>", 0));
        label_6->setText(QApplication::translate("Pong", "<html><head/><body><p><span style=\" font-size:14pt;\">Controle o pong com as setas (&lt;- e -&gt;) do teclado</span></p></body></html>", 0));
        label_2->setText(QApplication::translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">0</span></p></body></html>", 0));
        label_3->setText(QApplication::translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">x</span></p></body></html>", 0));
        label_4->setText(QApplication::translate("Pong", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">0</span></p></body></html>", 0));
        label->setText(QApplication::translate("Pong", "IP Server:", 0));
        radioButton->setText(QApplication::translate("Pong", "Player 1", 0));
        radioButton_2->setText(QApplication::translate("Pong", "Player 2", 0));
        pushButton->setText(QApplication::translate("Pong", "Conect", 0));
    } // retranslateUi

};

namespace Ui {
    class Pong: public Ui_Pong {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_PONG_H
