#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

//while循环的一个问题：在实际开发中，一个文件代码往往很长，这导致循环三要素在while循环中隔得很远
//增加了开发繁琐程度，所以实际开发往往使用for循环
//int main() {
//	int a = 0;//变量的初始化
//	while (a < 10) {//判断条件
//		a++;//调整
//	}
//	return 0;
//}

//int main() {//只打印0-9
//	int ch = 0;
//	while ((ch = getchar()) != EOF) {
//		if (ch < '0' || ch>'9')
//			continue;
//		putchar(ch);
//	}
//	return 0;
//}

//int main() {
//	int ch = getchar();//从键盘上获取一个字符，等同于scanf
//	putchar(ch);//把括号内的内容输出出去，等同于printf
//	return 0;
//}
//int main() {
//	int ch = 0;
//	while ((ch=getchar()) != EOF) {//EOF end of file 文件结束标准，本质上是一个-1
//		putchar(ch);
//	}
//}

//int main() {
//	int ret = 0;
//	char password[10] = { 0 };
//	printf("请输入密码：");
//	scanf("%d", password);//输入密码后内存缓冲区还剩一个回车字符
//	//输入的密码不能是123456 abc 因为scanf函数只会读取空格前的字符，
//	while (getchar() != '\n') {//用循环解决，直到缓冲区没有字符循环结束
//		;
//	}
//	//getchar();//取回车字符（清空缓冲区），但是一个getchar函数只能读取一次
//	printf("请确认（Y/X)");
//	ret = getchar();
//	if (ret == 'Y') {
//		printf("确认成功\n");
//	}
//	else {
//		printf("放弃确认\n");
//	}
//	return 0;
//}

//while循环
//int main() {//打印1-10
//	int a = 1;
//	while (a <= 10) {
//		if (a == 5)
//			break;//循环中遇见break，程序退出循环，循环不再继续
//		printf("%d\n", a);
//		a++;
//	}
//	return 0;
//}

//int main() {//打印1-10
//	int a = 1;
//	while (a <= 10) {
//		if (a == 5)
//			continue;//中止本次循环，本次循环中continue后面的代码不再执行，然后继续循环
//		printf("%d\n", a);
//		a++;
//	}
//	return 0;
//}
