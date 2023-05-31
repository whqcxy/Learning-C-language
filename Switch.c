//#define _CRT_SECURE_NO_WARNINGS
////switch语句-多个分支选择语句
//#include <stdio.h>
//
//int main() {
//	int n = 1;
//	int m = 2;
//	switch (n) {//switch语句也允许嵌套使用
//	case 1:
//		n++;
//	case 2:
//		m++;
//		n++;
//	case 3:
//		switch (n) {
//		case 1:n++;
//		case 2:m++; n++;
//			break;
//		}
//	case 4:
//		m++;
//		break;
//	default:
//		break;
//	}
//	printf("m=%d,n=%d\n", m, n);
//	return 0;
//}

//int main() {//判断那天是工作日和休息日
//	int worth = 0;
//	int day = 0;
//	scanf("%d", &day);
//	switch (day)//在switch语句中可以出现if
//	{//case后面不一定非要break
//	case 1:
//	case 2:
//	case 3:
//	case 4:
//	case 5:
//		printf("工作日");
//		break;
//	case 6:
//		if (worth == 0) {
//			printf("天气真好，可以去旅游了");
//		}
//	case 7:
//		printf("休息日");
//		break;
//	default://如果输入的内容都不匹配，则输出default，给用户一个提示
//		//default选项，可有可无，在处理可能出现非法选项时使用，
//		//推荐写上，如果不用提示时，可以不写default内的程序逻辑
//		//default，与case没有严格的顺序控制，建议把default写在最后
//		printf("输入错误\n");
//		break;
//	}
//	return 0;
//}

//int main() {//判断输入的是星期几
//	int day = 0;
//	scanf("%d", &day);
//	//if (day = 1) {//可以看出使用if语句写多分支的程序非常繁琐
//	//	printf("星期一");//我们可以使用switch语句来简化
//	//}else if (day=2){
//	//	printf("星期二");
//	//} else if(day=3){
//	//	printf("星期三");
//	//}...
//	switch (day)//定义变量day时switch规定必须使用整型（int)
//	{
//		case 1://case后面也必须使用整型数字/表达式结果为整型数字
//			printf("星期一");
//			break;
//		case 2:
//			printf("星期二");
//			break;
//		case 3:
//			printf("星期三");
//			break;
//		case 4:
//			printf("星期四");
//			break;
//		case 5:
//			printf("星期五");
//			break;
//		case 6:
//			printf("星期六");
//			break;
//		case 7:
//			printf("星期天");
//			break;//当程序运行break时，程序将自动跳转出程序块
//		//没有break,switch语句就无法自己跳出循环，会从程序入口一直运行到结束
//	}
//	return 0;
//}
