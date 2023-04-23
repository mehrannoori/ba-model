#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
using namespace std;


const 
int  N  =20000;  // number of nodes
int  m0 =    2;  // number of initial nodes
int  m  =    2;  // number of links of each new node
int  T  = N-m0;  // time steps

int  A[N][N];    // adjacency matrix
int  K  =  0;    // sum of all node's degrees


// functions decleration
void    init(void);
void    K_sum(void);
double  P_i(int);
void    make_adjmtrx(void);
void    save_adjmtrx(void);

/**********************************************************/
/*                          MAIN                          */
/**********************************************************/
int main(void){

    make_adjmtrx();

    return 0;
}


/**********************************************************/
/*                       FUNCTIONS                        */
/**********************************************************/
void init(void){
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            A[i][j] = 0;
        }
    }
    A[1][0] = 1; A[0][1] = 1;
}




void make_adjmtrx(void){
    srand(time(NULL));
    init();

    for(int t=0; t<T; t++){

        //cout << "\nstep: " << t << endl;
        
        K_sum();
        int new_node = m0 + t;
        //cout << "new node: " << new_node << endl;
        int edge = 0;
        
        while(edge != m){
            int indx = rand()%(m0+t);
            //cout << "target node: " << indx << endl;
            if(A[new_node][indx] == 0){
                double random = (float)rand()/RAND_MAX;
                //cout << "random number: " << random << endl;
                double p_i = P_i(indx);
                //cout << "P(i)=" << p_i << endl;
                if(random < p_i){
                    A[new_node][indx] = 1;
                    A[indx][new_node] = 1;
                    //cout << "----node " << new_node << " connected to " << indx << endl;
                    edge++;
                }
            }
        }
    }

    save_adjmtrx();
}




void K_sum(void){
    int sum = 0;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            sum += A[i][j];
        }
    }
    K = sum;
}




double P_i(int indx){
    float K_i = 0;
    for(int j=0; j<N; j++){
        K_i += A[indx][j];
    }
    
    return (float)K_i/K;
}



void save_adjmtrx(void){
    string filename = "adj" + to_string(N) + ".txt";
    ofstream output(filename);
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            output << A[i][j] << ",";
        }
        output << endl;
    }
    output.close();
}