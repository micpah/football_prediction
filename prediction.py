# from tensorflow.keras.utils import plot_model

from data import prepared_data
from model import Classifier, Regressor


if __name__ == "__main__":
    df = prepared_data(n_trend=8)

    print("\nRun multiclass classification")
    clf = Classifier(df)
    clf.run(epochs=100)

    print("\nRun regression (for home_score)")
    rgr1 = Regressor(df, target_name='home_score')
    rgr1.run(epochs=100)

    print("\nRun regression (for away_score)")
    rgr2 = Regressor(df, target_name='away_score')
    rgr2.run(epochs=100)

    # Plot and save model graphs
    # plot_model(clf.model, to_file='./doc/gfx/model_clf.png', show_shapes=True, rankdir="LR")
    # plot_model(rgr1.model, to_file='./doc/gfx/model_rgr_home.png', show_shapes=True, rankdir="LR")
    # plot_model(rgr2.model, to_file='./doc/gfx/model_rgr_away.png', show_shapes=True, rankdir="LR")

    # Plot validation curves
    clf.plot_validation_curve()
    rgr1.plot_validation_curve()
    rgr2.plot_validation_curve()

    # TODO: Pickle clf, rgr1, rgr2
    # TODO: Predict upcoming match day (of e.g. Bundesliga)
    # TODO: Proper Hyperparameter Tuning
    # TODO: Feature Engineering
