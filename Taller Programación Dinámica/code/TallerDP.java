import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class TallerDP  
{ 
    
    //Aproximación recursiva al algoritmo
    static public int minSumPartitionsNaive(int S[]){
        return minSumPartitionsNaive_Aux(S, 0, 0, S.length);
    } 
    static private int minSumPartitionsNaive_Aux(int S[], int s, int m, int size){
        //Caso Base: No hay elementos por revisar
        if (size == 0){
            return Math.abs(s - m);
        }
        else{
            //Si se incluye en A
            //Se disminuye la cantidad de elementos por revisar
            //Se agrega el elemento a la suma total de A
            int a = minSumPartitionsNaive_Aux(S, s + S[size - 1], m, size - 1);
            //Si se incluye en B
            //Se disminuye la cantidad de elementos por revisar
            //Se agrega el elemento a la suma total de B
            int b = minSumPartitionsNaive_Aux(S, s, m + S[size - 1], size - 1);
            //Se retorna la direrencia más pequeña
            if (a < b){
                return a;
            }else{
                return b;
            }
        }
    }

    //Algoritmo con memoización
    static public int minSumPartitionsMem(int S[]){
        //Declaro e inicializo la tabla de memoización
        int size = S.length;
        int total = 0;
        for (int i = 0; i < size; i++){
            total += S[i];
        }
        int M[][]= new int[size + 1][total + 1];
        return   minSumPartitionsMem_Aux(S, 0, 0, size, M);
    } 
    static private int minSumPartitionsMem_Aux(int S[], int s, int m, int size, int [][]M){
        //Se ha calculado?
        if (M[size][s] == 0){
            //Caso Base: No hay elementos por revisar
            if (size == 0){
                int x = Math.abs(s - m);
                M[size][s] = x;
            }
            else{
                //Si se incluye en A
                //Se disminuye la cantidad de elementos por revisar
                //Se agrega el elemento a la suma total de A
                int a = minSumPartitionsMem_Aux(S, s + S[size - 1], m, size - 1, M);
                //Si se incluye en B
                //Se disminuye la cantidad de elementos por revisar
                //Se agrega el elemento a la suma total de B
                int b = minSumPartitionsMem_Aux(S, s, m + S[size - 1], size - 1, M);
                //Se retorna la direrencia más pequeña
                if (a < b){
                    M[size][s] =  a;
                }else{
                    M[size][s] =  b;
                }
            }
        }
        return M[size][s];
    }
    //Versión Bottom-Up 
    static public int minSumPartitionsBottom(int S[]){
        //Declaro e inicializo la tabla de memoización
        int size = S.length;
        int total = 0;
        for (int i = 0; i < size; i++){
            total += S[i];
        }
        //True si es posible alcanzar el objetivo
        //Caso base, alcanzar un total de 0 con 0 elementos
        boolean M[][]= new boolean[size + 1][total + 1];
        for (int i = 0; i<= size; i ++){
            M[i][0] = true;
        }
        for (int i = 1; i <= size; i ++){
            for (int sum = 1; sum <= total; sum ++){
                M[i][sum] = M[i-1][sum];
                //Es posible incluir el elemento actual de la secuencia??
                if (sum >= S[i-1]){
                    M[i][sum] = M[i][sum] || M[i-1][sum-S[i - 1]];
                }
            }
        }
        //Búsco la suma total de la secuencia A óptima
        int sum = total/2;
        boolean found = false;
        while(sum>=0 && found == false){
            if (M[size][sum]){
                found = true;
            }else{
                sum --;
            }
        }
        //Retorno la diferencia óptima
        return total-2*(sum);
    }

    static public ArrayList<ArrayList<Integer>> binPartitionBT(List<Integer> S){
        int size = S.size();

        //Se guarda el valor total de la secuencia
        int total = 0;
        for (int i = 0; i < size; i++){
            total += S.get(i);
        }

        //Declaro e inicializo la tabla de memoización
        //Por defecto los arreglos del tipo boolean quedan inicializados en false
        boolean M[][] = new boolean[size + 1][total + 1];
        //Casos base, 0 elementos, secuencia vacía
        //Puedo lograr sumar 0 exlcuyendo todos los elementos
        for(int i = 0; i < size + 1; i ++){
            M[i][0] = true;
        }


        //Declaro e inicializo la tabla de BackTracking
        ArrayList<ArrayList<ArrayList<Integer>>> BT = new ArrayList<>();
        for (int i = 0; i < size + 1; i++){
            ArrayList<ArrayList<Integer>> col = new ArrayList<>();
            for (int j = 0; j < total + 1; j++){
                col.add(new ArrayList<>());
            }
            BT.add(col);
        }


        //Guardo que elementos en la secuencia A me permiten llegar a la un total desde 1 hasta la suma total de la secuencia
        for (int i = 1; i < size + 1; i++){
            for (int j = 1; j < total + 1; j++){
                if ((j - S.get(i -1)) >= 0){
                    //Puedo incluir el elemento i para sumar el valor j?
                    if(M[i -1][j - S.get(i -1)]){
                        //Se incluyen los elementos anteriores que me habían permitido sumar j - S[i - 1]
                        BT.get(i).get(j).addAll(BT.get(i - 1).get(j - S.get(i -1)));
                        //Ahora sumo el actual para alcanzar el valor j
                        BT.get(i).get(j).add(S.get(i - 1));
                        //Es posible alcanzar el valor j utilizando elementos en BT[i][j]
                        M[i][j] = true;
                    // Puedo alcanzar el valor sin incluir el elemento S[i -1]?
                    } else if(M[i - 1][j]){
                        //Incluyo todos los elementos que me habían ayudado a llegar al objetivo excluyendo el actual
                        BT.get(i).get(j).addAll(BT.get(i - 1).get(j));
                        //Es posible alcanzar el valor j utilizando elementos en BT[i][j]
                        M[i][j] = true;
                    }
                }else{
                    //Excluyo el elemento actual y agrego los que me habían ayudado antes
                    BT.get(i).get(j).addAll(BT.get(i - 1).get(j));
                    M[i][j] = M[i - 1][j];
                }
            }
        }


        //Se encuentra la posición de diferencia mínima
        int suma = total /2;
        boolean found = false;
        while(suma >= 0 && found == false){
            if (M[size][suma]){
                found = true;
            }else{
                suma --;
            }
        }

        //Guardo la secuencia A
        ArrayList<Integer> secA = BT.get(size).get(suma);
        //Agrego a la secuencia B todos los elementos que no hacen parte de la secuencia A
        ArrayList<Integer> secB = new ArrayList<>(S);
        for(int i = 0; i < secA.size(); i++){
            secB.remove(secA.get(i));
        }

        //Encapsulo las secuencias
        ArrayList < ArrayList <Integer> > retorno = new ArrayList<ArrayList<Integer>> ();
        retorno.add(secA);
        retorno.add(secB);

        System.out.println("Según el algoritmo con Backtracking la diferencia mínima es: " + (total - 2*suma));
        return retorno;

    }

    //int[] to List<Integer>
    private static List<Integer> createArrayList(int[] s1) {
        List<Integer> aux = new ArrayList<>();
        for (int i = 0; i < s1.length; i++){
            aux.add(s1[i]);
        }
        return aux;
    }
    

    public static void main (String[] args)  
    { 
        int S1[] = {1, 1, 1, 1, 100};
        List<Integer> S = createArrayList(S1);
        System.out.println("Test con " + S);
        System.out.println("Según el algoritmo Naive, la diferencia mínima es: " + TallerDP.minSumPartitionsNaive(S1));
        System.out.println("Según el algoritmo con Memoizacion, la diferencia mínima es: " + TallerDP.minSumPartitionsMem(S1));
        System.out.println("Según el algoritmo Bottom UP, la diferencia mínima es: " + TallerDP.minSumPartitionsBottom(S1));
        System.out.println("Las subsecuencias son: " + TallerDP.binPartitionBT(S));
        System.gc();

        System.out.println();
        System.out.println("---------------------------------------------------------");
        System.out.println();
    
        int S2[] = {10, 20, 30 , 40, 50};
        S = createArrayList(S2);
        System.out.println("Test con " + S);
        System.out.println("Según el algoritmo Naive, la diferencia mínima es: " + TallerDP.minSumPartitionsNaive(S2));
        System.out.println("Según el algoritmo con Memoizacion, la diferencia mínima es: " + TallerDP.minSumPartitionsMem(S2));
        System.out.println("Según el algoritmo Bottom UP, la diferencia mínima es: " + TallerDP.minSumPartitionsBottom(S2));
        System.out.println("Las subsecuencias son: " + TallerDP.binPartitionBT(S));
        System.gc();

        System.out.println();
        System.out.println("---------------------------------------------------------");
        System.out.println();
        
        int S3[] = {2, 2, 3, 4, 5, 9, 8, 4, 7};
        S = createArrayList(S3);
        System.out.println("Según el algoritmo Naive, la diferencia mínima es: " + TallerDP.minSumPartitionsNaive(S3));
        System.out.println("Según el algoritmo con Memoizacion, la diferencia mínima es: " + TallerDP.minSumPartitionsMem(S3));
        System.out.println("Según el algoritmo Bottom UP, la diferencia mínima es: " + TallerDP.minSumPartitionsBottom(S3));
        System.out.println("Las subsecuencias son: " + TallerDP.binPartitionBT(S));
        System.gc();

    }

    
} 
