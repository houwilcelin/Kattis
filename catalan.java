import java.math.BigDecimal;
import java.util.Scanner;

public class catalan {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int q = sc.nextInt();
        BigDecimal[] cat = new BigDecimal[5001];
        cat[0] = new BigDecimal(1);
        for (int j = 1; j <= 5000; j++) {
            BigDecimal d = new BigDecimal(2 * (2 * j + 1));
            cat[j] = cat[j - 1].multiply(new BigDecimal(4 * j - 2))
                    .divide(new BigDecimal(j + 1), BigDecimal.ROUND_HALF_DOWN);
        }
        for (int i = 0; i < q; i++) {
            System.out.println(cat[sc.nextInt()]);
        }

    }
}