from hmmlearn.hmm import GaussianHMM

def fit_hmm(X, n_components=3):
    model = GaussianHMM(n_components=n_components, covariance_type='full', n_iter=1000)
    model.fit(X)
    states = model.predict(X)
    return model, states