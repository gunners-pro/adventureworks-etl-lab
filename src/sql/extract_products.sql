SELECT dp.ProductKey, dp.ProductAlternateKey, dp.WeightUnitMeasureCode, dp.SizeUnitMeasureCode, dp.EnglishProductName, dp.StandardCost, dp.FinishedGoodsFlag,
    dp.Color, dp.SafetyStockLevel, dp.ReorderPoint, dp.ListPrice, dp.Size, dp.SizeRange, dp.Weight, dp.DaysToManufacture, dp.ProductLine, dp.DealerPrice,
    dp.Class, dp.Style, dp.ModelName, dp.EnglishDescription, dp.StartDate, dp.EndDate, dp.Status,
    dps.ProductSubcategoryKey, dps.ProductSubcategoryAlternateKey, dps.EnglishProductSubcategoryName, dps.ProductCategoryKey,
    dpc.ProductCategoryAlternateKey, dpc.EnglishProductCategoryName
FROM dbo.DimProduct AS dp
    INNER JOIN dbo.DimProductSubcategory AS dps ON dp.ProductSubcategoryKey = dps.ProductSubcategoryKey
    INNER JOIN dbo.DimProductCategory AS dpc ON dps.ProductCategoryKey = dpc.ProductCategoryKey