from my_project.df import my_df


def test_my_df():
    """Does it work?"""
    df = my_df()
    assert df.shape == (3, 2)
