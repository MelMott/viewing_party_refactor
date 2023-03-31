from viewing_party.movie import Movie
import pytest

def test_1():
    # Arrange/Act
    argo = Movie("Argo")
    horror = Movie("Horror")
    rate = Movie(8)



    # Assert
    assert argo.movie == "Argo"
    assert horror.genre == "Horror"
    assert rate.rating == 8
    