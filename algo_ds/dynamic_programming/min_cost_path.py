
def min_cost_path(cost):
    """

    Function to compute minimum cost path
    :param cost:
    :return:
    """
    path=[]
    
    for i in range(len(cost)):
        path.append([0]*len(cost[i]))

    path[0][0]=cost[0][0]

    for i in range(1,len(cost)):
        path[i][0]=path[i-1][0]+cost[i][0]

    for i in range(1,len(cost[0])):
        path[0][i]=path[0][i-1]+cost[0][i]

    print(path)

    for i in range(1, len(cost)):
        for j in range(1, len(cost[i])):
            path[i][j]=min(path[i-1][j-1],path[i-1][j],path[i][j-1])+cost[i][j]

    return path[len(path)-1][len(path[0])-1]


def trace_min_cost_path(cost):
    """
    Funtion to traace min cost path

    :param cost:
    :return:
    """
    

if __name__=="__main__":
    cost = [[1, 2, 3],         [4, 8, 2],         [1, 5, 3]]
    print(min_cost_path(cost))
