package challenge;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class CharacterRecongnition {
    public static void main(String[] args) {
        Scanner cin = new Scanner(System.in);
        ArrayList<Object> cubeList=new ArrayList<>();
        int row=0;
        int cloum=0;
        int cubeNumber;
        String temp=cin.nextLine();
        String[] tempString=temp.split(" ");
        int[] need={0,0,0};
        for (int i=0;i<3;i++) {
            need[i]=Integer.valueOf(tempString[i]);
        }
        row=need[0];
        cloum=need[1];
        cubeNumber=need[2];
        //读入cube
        for(int i=0;i<cubeNumber;i++){
            //跳过空行
            String noUse=cin.nextLine();
            int[][] tempCube=new int[row][cloum];
            for(int j=0;j<row;j++){
                //读入一行
                String rowString=cin.nextLine();
                char[] c=rowString.toCharArray();
                int number=0;
                //System.out.println(c.length);
                 for(int m=0;m<c.length;m++){
                        number =Integer.parseInt(String.valueOf(c[m]));
                        //System.out.println(number);
                    }
                for(int k=0;k<cloum;k++){
                    tempCube[j][k]=number;
                }    
            }
            //System.out.println(Arrays.deepToString(tempCube));
            cubeList.add(tempCube);
        }
        System.out.println(findSmallestDiff(cubeList));
    }

    public static int findSmallestDiff(ArrayList<Object> cubeLis) {
        int cubeNumber=cubeLis.size();
        int[][] cube1=(int[][]) cubeLis.get(0);
        //列数
        int cloum=cube1[0].length;
        //行数
        int row=cube1.length;
        //构造新的牛逼矩阵
        Object[][] nb=new Object[row][cloum];
        //遍历同时初始化
        for(int i=0;i<row;i++){
            for(int j=0;j<cloum;j++){
                int[]mark={0,0};
                nb[i][j]=mark;
                }
            }

        //开始逐个处理矩阵
        for (Object cube : cubeLis) {
            int[][] tempCube=(int[][]) cube;
            for(int i=0;i<row;i++){
                for(int j=0;j<cloum;j++){
                    int[]mark=(int[]) nb[i][j];
                    if (tempCube[i][j]==1) {
                        mark[0]=mark[0]++;
                    }else{
                        mark[1]=mark[1]++;
                    }
                    //mark还原
                    nb[i][j]=mark;
                }
            }
        }
        //处理完毕开始判定
        int totalMarkPoint=row*cloum;
        for(int i=0;i<row;i++){
            for(int j=0;j<cloum;j++){
                    int[] tempMark=(int[]) nb[i][j];
                    if (tempMark[0]==cubeNumber||tempMark[1]==cubeNumber) {
                        totalMarkPoint--;
                    }
                }
            }
        int border=(int) Math.ceil(log(cubeNumber,2)); 
        if (totalMarkPoint>border) {
            return border;
        }

        return 0;
    }

        static public double log(double value,double base) {
                    return Math.log(value) / Math.log(base);
                }
}