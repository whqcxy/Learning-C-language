#define _CRT_SECURE_NO_WARNINGS
//包含一个叫stdio.h的文件
//std-标准写法->standard input output

#include <stdio.h>//引入函数包stdio
////int是整型的意思
////main前面的int表示main函数调用返回一个int型
//int main() //main主函数-程序的入口，有且仅有一个
//{
//	//在这里完成任务
//	//在屏幕上输出
//	//函数printf->print function 是打印函数
//	//库函数是c语言本身提供使用的函数
//	//使用需调用
//	printf("hello,c!!!\n");
//	return 0;//返回0
//}


//int main()
//{
//	char ch = 'A';//创建了一块char类型内存，放入了一个ch,内容是A
//	 shout int age = 20;//创建了一块短整型类型内存，放入了一个age，内容是20
//	//short int 短整型
//	//long长整型
//	//int整型
//	//char字符数据类型
//	//float浮点型，小数型
//	//double 双浮点型
//	double d = 3.14;
//	float f = 0.6;
//	printf("%lf\n", d);
//	printf("%f\n", f);
//	printf("%c\n", ch);//%c ->打印字符格式的数据
//	printf("%d\n", age);//%d->打印整型十进制格式的数据
//	return 0;
//}

//int main()//不同的类型内存大小
//{
//	printf("%d\n", sizeof(char));//1
//	printf("%d\n", sizeof(int));//4
//	printf("%d\n", sizeof(long));//4
//	printf("%d\n", sizeof(float));//4
//	printf("%d\n", sizeof(double));//8
//	printf("%d\n", sizeof(long long));//8
//	printf("%d\n", sizeof(short));//2
//	return 0;
//}

//int main() {//定义变量：类型 变量名 = 数值；
//	short age = 16;//向内存申请2个字节=16bit位，用来存放20；
//	float weight = 96.5f;//向内存申请4个字节32bit位，用来存放96.5；
//  return 0;
//}

//int num = 10;//全局变量，定义在函数之外的变量，所有函数都可以使用
//int main()
//{
//	int num = 6;//局部变量，定义在函数内的变量，只能在函数内使用
//	printf("%d\n", num);//局部变量和全局变量的名字不要相同，容易误会，产生bug
//	//当名字相同时，局部变量优先
//	return 0;
//}

//int a = 10;//全局变量
//int main()
//{
//	{
//		int a = 20;//局部变量
//	}
//	printf("%d\n", a);//打印函数和局部变量不在同一代码块，无法调用，但可以调用全局变量，打印为10
//	return 0;
//
//}


//int main()//计算两个数的和
//{
//	int num1 = 0;
//	int num2 = 0;
//	int sum = 0;
//	//输入函数
//	scanf("%d%d", &num1, &num2);//取地址符&
//	//C语言语法规定，变量要定义在当前代码块的最前面
//	sum = num1 + num2;
//	printf("sum = %d\n",sum);
//	return 0;
//}


////int a = 1;//全局变量的作用域是整个工程,整个工程都可以使用a
////在同一原文件下的其他.c文件中全局变量依旧可以使用，但必须声明标识符
//extern int a;//声明extern 外部符号; 
//void test() 
//{//函数test，调用a值
//	printf("test()= %d\n", a);
//}
//int main()
//{//代码块1
//	test();
//	int b = 2;//局部变量b的作用域是代码块1，2,只有代码块1，2可以使用b
//	printf("%d\n", a);
//	printf("%d\n", b);
//	{//代码块2
//		int c = 3;//局部变量c的作用域是代码块2,只有c所属的代码块2可以使用
//		printf("%d\n", a);
//		printf("%d\n", b);
//		printf("%d\n", c);
//	}
//		return 0;
//}
//


#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

//结构体：关键字struct
//描述如：人，书等复杂对象
//描述人需要身高，体重，年龄，身份号码等各种信息
//如何描述复杂对象需要使用结构体——我们创造的一种类型
struct Book
{
	char name[20];//类型 对象名[空间大小];
	short value;
};

//int main() {
//	//利用结构体类型-创建一个该类型的结构体变量
//	struct Book b1 = { "C语言程序设计",40 };
//	b1.value = 10;//这样可以改变是因为value是一个变量，name不可以这样因为name是一个数组
//	strcpy(b1.name, "数据结构");//数组名本质上是一个地址,必须使用strcopy函数（字符串拷贝）来改变，
//	//使用strcopy需要引入string.h包,使用的结构是strcopy（变量.对象名，覆盖的新内容）;
//	printf("%s\n",b1.name);
//	//struct Book* pd = &b1;//把b1的指针地址赋给pd
//	//printf("%s\n", pd->name);//简化利用指针把书名和价格打印出来
//	//printf("%d\n", pd->value);//"->"指向符
//	//printf("%s\n", (*pd).name);//利用指针把书名和书价格打印出来
//	//printf("$d\n", (*pd).value);
//	//. 结构体变量.成员
//	// -> 结构体指针->成员
//	//printf("书名:%s\n", b1.name);
//	//printf("价格:%d\n", b1.value);
//	return 0;
//}

////指针
////如何产生地址？
////为什么电脑分为32位和64位？
////因为32位电脑由32根数据线组成，当通电时，正电与负电的0，1组合排列出从1到2^32种组合，从而产生了2^32个地址
////同理64位产生2^64个地址
////一个地址有多大呢？
////1bit大小，但是这样太小只有0.5Gb内存，所以一个地址分配8个bit，也就是1个byte。
////所以32位电脑最多支持4Gb内存，
////一个指针大小，32位是4byte，64位是8比特
//int main() {
//	int a = 10;//申请四个字节
//	int* p = &a;//&a取地址,int*类型 存地址,其类型取决于p指向的值是什么类型
//	printf("%p\n", p);
//	//*p;//*——解引用操作符
//	*p = 20;//根据p找到a地址，然后把20赋给a
//	printf("%d\n", sizeof(p));
//	printf("%d\n", a);//输出值为20；
//	   //有一种变量是用来存放地址的——指针变量
//	printf("%p\n", &a);//地址为00EFFBE0->1110 1111 1111 1010 1110 0000——一个随机地址
//	return 0;//取地址符%p
//}
//
//int main() {
//	double a = 3.14;
//	double* p = &a;
//	printf("%d\n", sizeof(a));//double大小8
//	printf("%d\n", sizeof(p));//指针大小4
//}


//#define MAX 10//定义标识符常量
////#define 可以定义宏-带参数
//int Max(int x, int y) {
//	if (x > y)
//		return x;
//	else
//	{
//		return y;
//	}
//}
//
////宏的定义
//#define MAX(X,Y) (X>Y?X:Y)
//
//int main() {
//	int a = 10;
//	int b = 20;
//	//函数的方式
//	int max = Max(a, b);
//	printf("%d\n", max);
//	//宏的方式
//	max = MAX(a, b);
//	//编译器替换了后变成了 max = (a>b?a:b);
//	printf("max =%d\n", max);
//	return 0;
//}


////跨文件调用函数必须声明外部函数
//extern int Add(int, int);//声明静态函数后调用失败。
//int main()//static修饰函数
//{
//	int a = 10;
//	int b = 20;
//	int sum = Add(a, b);
//	printf("sum = %d\n",sum);
//	return 0;
//}

//int main() {
//	extern g_val;//关键字extern，调用其他同一源文件下其他文件中的全局变量
//	printf("%d\n", g_val);//调用失败，因为g_val是静态全局变量，无法跨文件调用
//	return 0;
//}

//void test() {
//	static int a = 1;//静态局部变量，a的生命周期变长，不会因为程序结束而结束
//	a++;//a值会累计
//	printf("%d\n", a);
//}
//
//int main() {
//	int i = 0;
//	while (i < 5) {
//		test();
//		i++;
//	}
//	return 0;
//}

//int main() {
//	
//	register int a = 10; //建议把a定义成寄存器变量
//	unsigned int num = 1;//定义一个无符号数，即使为负数，num也为正数
//	//struct结构体关键字
//	//union,联合体关键字
//	//typedef,类型重定义
//	typedef unsigned int u_int;//将unsigned int 类型重定义为u_int，为unsigned int 创建一个别名，类似于软链接
//	static int a;//静态局部变量，
//	return 0;
//}

//int main() {
//	int a = 0;
//	int b = 0;
//	int max = 0;
//	scanf("%d%d",&a,&b);
//	max = (a > b ? a : b);
//	printf("%d\n", max);
//	return 0;
//}

//int main() {
//	//真——非0
//	//假——0
//	//&&——逻辑与,两个里面全是真为真
//	//||——逻辑或，两个里面有一个真为真
//	int a = 3;
//	int b = 4;
//	int c = a && b;
//	printf("%d", c);
//	return 0;
//}

//int main() {//强制类型转换，一般不推荐使用
//	int a = (int)3.14;
//	return 0;
//}

//int main() {
//	int a = 10;
//	int b = a++;//后置++，先赋值再++ 11 10
//	int b = ++a;//前置++，先++再赋值 11 11
//	int b = a--;//后置--，先赋值再-- 9 10
//	int b = --a;//前置--，先--再赋值 9 9
//	printf("a = %d b = %d", a, b );
//	return 0;
//}

//int Arr(int x, int y) {
//	if (x > y) {
//		return x;
//	}
//	else
//	{
//		return y;
//	}
//}
//
//int main() {
//	int num1 = 0;
//	int num2 = 0;
//	printf("请输入两个数：\n");
//	scanf("%d%d", &num1, &num2);
//	int arr = Arr(num1, num2);
//	printf("较大值是：");
//	printf("%d\n", arr);
//	return 0;
//}

//int main() {
//	int num1 = 0;
//	int num2 = 0;
//	printf("请输入两个数");
//	scanf("%d%d", &num1, &num2);
//	if (num1>num2)
//	{
//		printf("数字1大");
//	}
//	else {
//		printf("数字2大");
//	}
//	return 0;
//}

//int main() {
//	int a = 10;
//	int arr[10] = { 0 };
//	int sz=sizeof(arr) / sizeof(arr[0]);//计算数组中元素个数
//	printf("%d\n", sz);
//	printf("%d\n", sizeof(a));//sizeof计算的是变量/类型所占空间的大小，单位是字节
//	printf("%d\n", sizeof(int));
//	printf("%d\n", sizeof a);
//	printf("%d\n", sizeof arr);
//	return 0;
//}

////初识数组
//int main() {
//	int test[10] = {1,2,3,4,5,6,7,8,9,10};//定义一个长度为10的int型数组，
//	//下标从0开始，以此递增，最大的那个下标是n-1
//	int i = 0;
//	while (i<10)
//	{
//		printf("%d\n", test[i]);
//		i++;
//	}
//	//printf("%d\n", test[2]);//用下标的方式访问数组元素
//	//char all[20];
//	return 0;
//}

////初学函数
////封装函数
//int add(int x, int y)/*函数名*/
//{
//	//函数体
//	int z = x + y;
//	return z;
//}
//int main() {//调用函数
//	int a = 10;
//	int b = 20;
//	int sum = add(a, b);
//	printf("%d\n", sum);
//	return 0;
//}

//int main() {//初识while循环
//	int line = 0;
//	while (line <= 2000) {
//		printf("%d", line);
//		printf("敲一行代码。");
//		line++;
//	
//	if (line>2000){
//		printf("给你一个好offer");
//		}
//	else{
//		printf("还要加把劲！！！\n");
//		}
//	}
//	return 0;
//}

//int main() {//初学if判断
//	int input = 0;
//	printf("好好学习吗？(1/0)>:");
//	scanf("%d", &input);
//	if (input == 1) {
//		printf("好offer\n");
//	}
//	else
//	{
//		printf("卖红薯");
//	}
//	return 0;
//}


//int main() {
//	printf("%d\n", strlen("c:\test\32\test.c"));
//	return 0;
//}


//int main() {
//	printf("\\test");//前面加一个斜杠，防止出现转译
//	printf("%c\n", '\'');//无斜杠单引号无法单独运行
//	return 0;
//}


//int main() {
//	char arr1[] = "abc";//3
//	char arr2[] = { 'a','b','c'};//随机值
//	printf("%d\n", strlen(arr1));//strlen-string length-计算字符串长度
//	printf("%d\n", strlen(arr2));
//}


//int main()
//{
//
//	char arr[] = "abc";//数组
//	char arr1[] = {'a','b','c',0};//或者{'a','b','c','\n'}末尾放的不是0是\0，\0是字符串的结束标志
//	printf("%s\n", arr);//打印字符串用%s
//	printf("%s\n", arr1);
//	return 0;
//}


//字符串
//int main()
//{
//	"abcdef";//字符串
//	"";//空字符串
//	return 0;
//}


//枚举常量--可一一列举，如性别，三原色：红黄蓝，星期
//枚举关键字--enum
//enum  Sex
//{
//	MALE,//0
//	FEMALE//1
//	//有值，不可改变
//};
//
//enum Color {
//	RED,
//	YELLOW,
//	BLUE
//};
////MALE,FEALE——枚举常量
//int main()
//{
//	enum Color c = RED;
//	c = YELLOW;
//	printf("%d\n", c);
//	/*enum Sex s = MALE;
//	printf("%d\n", MALE);
//	printf("%d\n", FEMALE);*/
//	return 0;
//}


////#define 定义的标识符常量
//#define MAX 5 //MAX为一个常量
//int main() {
//	int arr[MAX] = { 0 };
//	printf("%d\n", MAX);
//	return 0;
//}


//int main() {
//	const int num = 3;//const-常属性，const修饰的常变量，num还是变量，但有了常量的属性，不可重新赋值。
//	printf("%d\n", num);
//
//	printf("%d\n", num);
//	5;//字面常量
//	return 0;
//}
