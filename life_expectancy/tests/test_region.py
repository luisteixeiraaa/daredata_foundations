from life_expectancy.region import Region


def test_regions():
    """Test for the valid countries.
    Ensure that countries belong to Region in their shortform.
    """
    countries = Region.valid_countries()
    # Test that all returned values are Region enums
    assert all(
        (isinstance(country, Region) and len(country.value) == 2)
        for country in countries
    )
