SELECT dc.CustomerKey, dc.CustomerAlternateKey, dc.Title, dc.FirstName, dc.MiddleName, dc.LastName, dc.NameStyle, dc.BirthDate, dc.MaritalStatus,
    dc.Suffix, dc.Gender, dc.EmailAddress, dc.YearlyIncome, dc.TotalChildren, dc.NumberChildrenAtHome, dc.EnglishEducation, dc.EnglishOccupation,
    dc.HouseOwnerFlag, dc.NumberCarsOwned, dc.AddressLine1, dc.AddressLine2, dc.Phone, dc.DateFirstPurchase, dc.CommuteDistance,
    dg.GeographyKey, dg.City, dg.StateProvinceCode, dg.StateProvinceName, dg.CountryRegionCode, dg.EnglishCountryRegionName, dg.PostalCode
FROM dbo.DimCustomer AS dc
    INNER JOIN dbo.DimGeography AS dg
    ON dg.GeographyKey = dc.GeographyKey