import java.util.Random;
import java.util.Scanner;

/**
 * Pseudo code:
 * for i=1:end-1
 *  set the index of the smallest element is i
 *  for j=i:end
 *   if the element at j is smaller than element at the index of the smallest element, then set the index of the smallest element is j
 *  endfor
 *  swap the element at i with the smallest element
 * endfor
 */

public class Solution {
    public static void main(String[] args) {
        Solution sol = new Solution();
        Random rd = new Random();
        Scanner sc = new Scanner(System.in);
        int n;
        System.out.println("Size of array (n):");
        n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; ++i) {
            a[i] = rd.nextInt();
        }

        System.out.println("Original array: ");
        sol.printArray(a);
        long startTime = System.nanoTime();
        sol.selectionSort(a);
        long stopTime = System.nanoTime();
        System.out.println("After sort:");
        sol.printArray(a);
        long executionTime = stopTime-startTime;
        System.out.println("Execution time: " + executionTime + " nanoseconds = " + (double) executionTime/1_000_000_000 + " seconds");
        // sol.drawPlot();
    }

    public void printArray(int[] a) {
        for (int i = 0; i < a.length; ++i) {
            System.out.print(a[i]);
            if (i != a.length-1){
                System.out.print(" ");
            }
            else {
                System.out.print("\n");
            }
        }
    }

    public void swap(int[] a, int u, int v) {
        int tmp = a[u];
        a[u] = a[v];
        a[v] = tmp;
    }

    public void selectionSort(int[] a) {
        int n = a.length;
        for (int i = 0; i < n-1; ++i) {
            int indexOfMinElement = i;
            for (int j = i+1; j < n; ++j) {
                if (a[j] < a[indexOfMinElement]) {
                    indexOfMinElement = j;
                }
            }
            swap(a, i, indexOfMinElement);
        }
    }

    public long calculateExecutionTime(int arraySize) {
        Random rd = new Random();
        int[] a = new int[arraySize];
        for (int i = 0; i < arraySize; ++i) {
            a[i] = rd.nextInt();
        }
        long startTime = System.nanoTime();
        selectionSort(a);
        long stopTime = System.nanoTime();
        return stopTime-startTime;
    }

    public void drawPlot() {
        int[] arraySizes = new int[10];
        long[] executionTimes = new long[arraySizes.length];
        for (int i = 0; i < arraySizes.length; ++i) {
            arraySizes[i] = 10*(i+1);
            executionTimes[i] = calculateExecutionTime(arraySizes[i]);
        }
        // printArray(arraySizes);
    }
}