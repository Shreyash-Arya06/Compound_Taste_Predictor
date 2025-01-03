# We will create a function to prdict similarity between the compounds.
class WeightedEditDistance:
    def __init__(self, seq1_list, seq2_list, ins_weight = 1, del_weight = 1, subs_weight = 1, mode = 0):
        self.seq1_list = seq1_list
        self.seq2_list = seq2_list
        self.ins_weight = ins_weight
        self.del_weight = del_weight
        self.subs_weight = subs_weight
        self.mode = mode

    def calculateDist(self, m, n, seq1, seq2):
        grid = [[0 for i in range(m+1)] for j in range(n+1)]        # Initializing the matrix
        
        for i in range(n+1):
            for j in range(m+1):
                # First row and column of the matrix is initialized
                if (j == 0):
                    grid[i][j] = i * self.del_weight
                elif (i == 0):
                    grid [i][j] = j * self.ins_weight
                elif (seq1[i-1] == seq2[j-1]):
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = min(grid[i-1][j-1] + self.subs_weight, grid[i-1][j] + self.del_weight, grid[i][j-1] + self.ins_weight)

        return grid[n][m]

    def getScore(self):
        scores = []
        final_score = 0
        if (self.mode == 0):
            for smiles in self.seq1_list:
                total = 0
                count = 0
                n = len(smiles)
                for compare_smiles in self.seq2_list:
                    m = len(compare_smiles)
                    # The code will calculate similarity only when the SMILES' length difference will be atmost 5, because otherwise they are dissimilar.
                    if (abs(m-n) <= 5):
                        dist = self.calculateDist(m, n, smiles, compare_smiles)
                        cost = 1 - (dist/max(m, n))
                        total += cost
                        count += 1
                if (count > 0):
                    score = total/count
                    scores.append(score)
            
            for val in scores:
                final_score += val
            
            return (final_score/len(scores))
        else:
            smiles = self.seq1_list
            n = len(smiles)
            for compare_smiles in self.seq2_list:
                m = len(compare_smiles)
                if (abs(m-n) <= 5):
                    dist = self.calculateDist(m, n, smiles, compare_smiles)
                    cost = 1 - (dist/max(m, n))
                    scores.append(cost)

            if (len(scores) == 0):
                return 0
            else:
                scores.sort(reverse=True)
                return scores[0]
            