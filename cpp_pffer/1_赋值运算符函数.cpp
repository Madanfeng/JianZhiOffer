#include<iostream>
using namespace std;
/*
    如下为类型CMyString的声明，请为该类型添加赋值运算符函数。
*/
class CMyString
{
private:
    char * m_pData;
public:
    CMyString(char * pData = nullptr);
    CMyString(const CMyString& str);
    ~CMyString(void);
};


int main()
{

    return 0;
}