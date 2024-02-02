import numpy as np
class KFoldCrossValidation:
    """
    Modella la tecnica di k-fold cross validation per la suddivisione di un dataset in training set e test set.
    """
    def __init__(self, data, target, K):
        """
        Costruttore

        Parameters
        ----------
        data : pandas.DataFrame
            il dataset da suddividere
        target : pandas.Series
            la serie di valori target
        K : int
            il numero di fold


        Returns
            ----
        None
        """
        self.data = data
        self.target = target
        self.K = K
        self.fold = []
    def split(self):
        """
        Suddivide il dataset in training set e test set.

        Returns
        -------
        list
            una lista di tuple, ognuna delle quali contiene:
            - il training set
            - il test set
            - i valori target del training set
            - i valori target del test set

        """
        #assicura che la sequenza di numeri casuali generata sia sempre la stessa per lo stesso valore di random_state
        np.random.seed(self.random_state)
        #generazione degli indici
        indices = np.random.permutation(self.data.index)
        #generazione dei fold
        fold_size = int(len(self.data)/self.K)
        for i in range(self.K):
            test_index = indices[i*fold_size:(i+1)*fold_size] #seleziona gli indici per il test set
            train_index = indices[~np.isin(indices, test_index)]
            #generazione dei train set e test set
            train = self.data.loc[train_index] #loc seleziona le righe con gli indici indicati
            test = self.data.loc[test_index]
            #generazione dei target
            train_target = self.target.loc[train_index]
            test_target = self.target.loc[test_index]
            self.fold.append((train, test, train_target, test_target))
        return self.fold