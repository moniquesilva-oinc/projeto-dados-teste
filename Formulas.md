Saldo Acumulado é um campo calculado igual a =SOMARPRODUTO(($B$2:$B$100=B2)*($A$2:$A$100<=A2)*$C$2:$C$100)
-SOMARPRODUTO(($B$2:$B$100=B2)*($A$2:$A$100<=A2)*($D$2:$D$100="Entrada")*($B$2:$B$100="NIJ")*($A$2:$A$100<=DATA(2026;5;31))*$C$2:$C$100*0,3)
-SOMARPRODUTO(($B$2:$B$100=B2)*($A$2:$A$100<=A2)*($D$2:$D$100="Entrada")*($B$2:$B$100="NIJ")*$C$2:$C$100*0,3)
-SOMARPRODUTO(($B$2:$B$100=B2)*($A$2:$A$100<=A2)*($D$2:$D$100="Entrada")*($B$2:$B$100="DIAG")*$C$2:$C$100*0,3)
-SOMARPRODUTO(($B$2:$B$100=B2)*($A$2:$A$100<=A2)*($D$2:$D$100="Entrada")*($B$2:$B$100="Geral")*$C$2:$C$100*0,1)

Adm é um campo calculado igual a
SUM(
  CASE
    WHEN Tipo(Natureza) = "Entrada" AND   TRIM(Projeto) IN ("NIJ", "DIAG") THEN  Valor(R$) * -0.3
    WHEN Tipo(Natureza) = "Entrada" AND   TRIM(Projeto) IN ("Geral") THEN  Valor(R$) * -0.1
    ELSE 0
  END
)

Repasse CF é um campo calculado igual a
SUM(
  CASE
    WHEN Tipo(Natureza) = "Entrada" AND   TRIM(Projeto) IN ("NIJ") THEN  Valor(R$) * -0.3
    ELSE 0
  END
)