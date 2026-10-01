# Orion Foods: Capital Structure Recommendation

## Corporate Finance Case Analysis

### Executive recommendation

**Recommendation: Option D — approximately €761 million of debt, or 38.0% of total capital, with an estimated average interest rate of 5.52%.** Option D is a proposed intermediate structure, not one of the three alternatives in the case. It is calculated by using Excel Goal Seek to target **5.0× interest coverage in the recession scenario**.

At the target, annual interest expense is €42 million and the annual tax shield is €10.5 million. Coverage is 8.57× in a strong year, 7.14× in a normal year and 5.00× in a recession. This is deliberately more conservative than Option B, whose recession coverage is 3.50×, while still increasing leverage and the tax shield above Option A. The proposed 38.0% debt-to-capital ratio is at the lower end of the peer range of 38%–55%.

The case’s formal warning threshold is below 2.0× in a recession; the 5.0× target is the group’s stricter risk preference, not a requirement imposed by the case. Because borrowing costs for a custom Option D are not provided, its rate is estimated by linear interpolation between Options A and B. The result should therefore be presented as a transparent, assumption-based recommendation—not as an exact optimum.

## 1. Company context and decision

Orion Foods is a publicly listed European producer of packaged food. It operates in a mature industry with historically stable demand, although sales and margins decline during economic downturns. The company owns most of its manufacturing facilities and distribution centers, giving it a substantial tangible-asset base.

In the latest financial year, Orion generated €2.5 billion in revenue and €300 million in EBIT. It has €500 million of existing debt at an average rate of 5%, implying €25 million of annual interest expense. Its market value of equity is €1.5 billion, so current debt / total capital is 25%. The corporate tax rate is 25%, and Orion expects sufficient taxable income to use interest deductions fully.

The proposed recapitalizations use any debt raised above the existing €500 million to repurchase shares. They change the financing mix, not operating assets or EBIT. The operating scenarios are €360 million of EBIT in a strong year, €300 million in a normal year and €210 million in a recession. The board considers recession interest coverage below 2.0× a significant financial risk.

A possible €200 million automated production facility may become available in approximately two years. The project is not approved and may never proceed, but it is expected to have a positive NPV of €30 million if market conditions develop as expected.

## 2. Quantitative analysis of Options A–C

The annual interest tax shield is interest expense multiplied by the 25% corporate tax rate. Interest coverage is EBIT divided by annual interest expense.

| Measure | Option A | Option B | Option C |
|---|---:|---:|---:|
| Total debt | €500m | €1,000m | €1,500m |
| Debt / total capital | 25% | 50% | 75% |
| Average interest rate | 5.0% | 6.0% | 9.0% |
| Annual interest expense | €25m | €60m | €135m |
| Annual interest tax shield | €6.25m | €15.00m | €33.75m |
| Coverage — strong year (EBIT €360m) | 14.40× | 6.00× | 2.67× |
| Coverage — normal year (EBIT €300m) | 12.00× | 5.00× | 2.22× |
| Coverage — recession (EBIT €210m) | 8.40× | 3.50× | 1.56× |

The tax shield rises with leverage: Option B provides €8.75 million more per year than A, while Option C provides a further €18.75 million over B. These are tax savings, not the total net value created by debt. Expected distress costs, reduced flexibility and incentive effects also matter.

Option B remains above the board’s formal 2.0× recession threshold, but its 3.50× coverage is below the more conservative 5.0× target proposed here. Option C breaches the board’s threshold at 1.56×.

## 3. Option D: Goal Seek design

The case does not state the interest rate for a debt level between A and B. To estimate Option D, assume the average borrowing rate increases linearly from 5.0% at €500 million of debt to 6.0% at €1,000 million:

- `Rate(D) = 5.0% + [(D − €500m) / €500m] × 1.0 percentage point`, for debt between €500m and €1,000m.
- `Interest expense(D) = D × Rate(D)`.
- Set recession interest coverage to `€210m EBIT / Interest expense(D) = 5.0×`.

Using Excel Goal Seek, set the recession-coverage cell to **5.0** by changing total debt. This gives approximately:

| Option D output | Goal Seek estimate |
|---|---:|
| Total debt | **€760.7m** (approximately €761m) |
| Estimated average interest rate | **5.52%** |
| Annual interest expense | **€42.0m** |
| Annual interest tax shield at 25% | **€10.5m** |
| Debt / total capital, assuming total capital remains €2.0bn | **38.0%** |
| Coverage — strong year (EBIT €360m) | **8.57×** |
| Coverage — normal year (EBIT €300m) | **7.14×** |
| Coverage — recession (EBIT €210m) | **5.00×** |

The €2.0 billion total-capital assumption is implied by the ratios in Options A–C. Option D adds about €260.7 million of debt over A and has €4.25 million more annual tax shield than A. Compared with B, it uses about €239.3 million less debt, has €18 million less annual interest expense and sacrifices €4.5 million of annual tax shield.

**Sensitivity:** If the rate were held constant at 5.0%, a 5.0× recession-coverage target would imply debt of €840 million and debt / total capital of 42%. The recommended €761 million estimate instead recognizes the case’s rising cost of debt as leverage increases. The lender’s actual pricing would be needed to refine Option D.

**Important interpretation:** If the target were 5.0× coverage in a *normal* year, Option B already meets it exactly (`€300m / €60m = 5.0×`). Option D is designed to achieve 5.0× in the *recession* scenario because the group’s concern is downside risk.

## 4. Debt capacity and comparable companies

### Factors supporting additional debt

Orion’s mature operations, historically stable demand, tangible assets and consistent profitability support debt capacity. Its taxable income is expected to be sufficient to use interest deductions. There are no major debt maturities or committed acquisitions in the next three years, and normal EBIT can support additional interest expense.

### Factors limiting additional debt

Sales and margins decline in downturns while interest obligations remain fixed. The board identifies coverage below 2.0× in a recession as significant risk. Higher leverage increases the borrowing rate under the case assumptions and reduces capacity to respond to shocks or future investment opportunities.

### Peer evidence

| Comparable company | Debt / total capital | Interest coverage |
|---|---:|---:|
| Alpha Foods | 38% | 7.2× |
| Bella Consumer | 44% | 6.1× |
| Continental Foods | 51% | 5.0× |
| Delta Brands | 55% | 4.4× |
| **Simple peer average** | **47%** | **5.7×** |

Option D’s 38.0% leverage is at the lower boundary of the peer range and below the 47% simple average. Its normal-year coverage of 7.14× is within the peer range and near its upper end. Peer coverage is not identified as recession coverage, so it is a benchmark rather than a direct stress-test comparison. These data support D as a conservative but plausible structure.

## 5. Incentives, investment and capital-structure theory

### Free-cash-flow discipline

Orion has retained substantial free cash flow and invested some in diversification projects earning below the returns of its core operations. Moderate debt service can reduce discretionary cash for low-return expansion and discipline management. Because the proceeds above existing debt are used for a share repurchase, the recapitalization distributes cash while committing Orion to future interest payments.

### Debt overhang and the possible plant

The possible €200 million facility has an expected positive NPV of €30 million but is unapproved. Excessive leverage today could make Orion unable or unwilling to finance a positive-NPV project later. If new investment partly benefits existing creditors by making their claims safer, shareholders may be reluctant to provide new equity. This is the debt-overhang or underinvestment problem. Option D preserves more room than B or C while avoiding the assumption that the company should raise the project’s cost today.

### Risk shifting / asset substitution

At very high leverage, shareholders may prefer projects with unusually high upside and substantial downside: shareholders retain much of the upside, while creditors bear part of the downside through a higher probability of default. This conflict is known as risk shifting or asset substitution. Option C creates the strongest concern; Option D reduces, but does not eliminate, the conflict.

### Trade-off theory and financial flexibility

The trade-off theory balances the interest tax shield against expected distress costs and other costs of debt. The tax shield alone does not identify the optimal leverage ratio. Option A maximizes financial flexibility but forgoes tax benefits and may leave low-return discretionary spending insufficiently constrained. Option C maximizes the tax shield but sacrifices too much coverage and flexibility. Option D reflects a more conservative risk appetite than B while still adding moderate leverage over A.

## 6. Comparison and recommendation

| Criterion | Option A | Option D (proposed) | Option B | Option C |
|---|---|---|---|---|
| Debt / total capital | 25% | **38.0%** | 50% | 75% |
| Annual tax shield | €6.25m | **€10.5m** | €15.0m | €33.75m |
| Normal-year coverage | 12.00× | **7.14×** | 5.00× | 2.22× |
| Recession coverage | 8.40× | **5.00×** | 3.50× | 1.56× |
| Financial flexibility | Highest | **High / moderate** | Medium | Lowest |
| Main concern | Conservative; weaker cash discipline | Lower shield than B; pricing is estimated | Below the group’s 5.0× recession target | Below the board’s 2.0× risk threshold |

**Recommendation:** adopt Option D as a conservative intermediate structure. It meaningfully increases debt and the tax shield over A, but preserves a 5.0× recession coverage target and keeps leverage at the low end of the peer range. Option B is above the board’s formal minimum coverage threshold, but it does not satisfy the group’s more cautious stress-coverage objective. Option C is not recommended because it breaches the board’s threshold and creates more severe flexibility and incentive concerns.

The 5.0× recession target is a deliberate management judgment, not a requirement stated in the case. It should be revisited if actual borrowing terms differ, the plant is approved, or the business outlook changes. Without probability-weighted distress costs and confirmed debt pricing, no exact optimal ratio can be proven.

## Conclusion

A moderate increase in leverage is justified, but maximum leverage is not. **Option D—approximately €761 million of debt at an estimated 5.52% average rate—is the group’s recommended balance**, conditional on the stated interpolation assumption and a 5.0× recession-coverage target.
