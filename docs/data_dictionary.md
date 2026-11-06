# Data Dictionary

## AI Financial Contagion and Geopolitical Risk Engine

**Version:** 0.1.0  
**Author:** Harsh Singh  
**Status:** Proposed Data Specification

---

## 1. Purpose

This document defines the proposed data variables,
their meanings, measurement units, frequencies
and potential data providers.

The actual availability, licensing and historical
coverage of every variable must be verified
before empirical implementation.

## 2. Data Modalities

The proposed architecture integrates six modalities:

1. Financial Market Data
2. Macroeconomic Data
3. Geopolitical Event Data
4. Financial Network Data
5. Textual Intelligence
6. Alternative Data

## 3. Financial Market Variables

| Variable | Definition | Unit | Frequency | Potential Source |
|---|---|---|---|---|
| equity_return | Percentage change in equity index | % | Daily | Exchange, licensed vendor |
| equity_volatility | Equity return volatility | % annualised | Daily | Market data provider |
| trading_volume | Traded market quantity | Shares/contracts | Daily | Exchange |
| bond_yield | Government bond yield | % | Daily | Central bank, vendor |
| bond_spread | Yield difference between instruments | Basis points | Daily | Market data provider |
| sovereign_cds | Sovereign credit default swap spread | Basis points | Daily | Licensed vendor |
| fx_return | Foreign exchange return | % | Daily | Central bank, vendor |
| commodity_return | Commodity price return | % | Daily | Exchange, vendor |
| vix_level | Implied equity volatility index | Index points | Daily | Cboe |
| capital_flow | Portfolio and FDI flows | Currency units | Monthly/Quarterly | IMF BOP, IIF |

## 4. Macroeconomic Variables

| Variable | Definition | Unit | Frequency | Potential Source |
|---|---|---|---|---|
| gdp_growth | Real GDP growth | % | Quarterly | IMF, World Bank |
| inflation | Consumer price inflation | % | Monthly | National statistics |
| unemployment | Unemployment rate | % | Monthly/Quarterly | ILO, national agencies |
| policy_rate | Central bank policy rate | % | Daily/Decision date | Central banks |
| public_debt | Government debt | Currency or % GDP | Quarterly/Annual | IMF, World Bank |
| fiscal_balance | Government fiscal balance | % GDP | Annual/Quarterly | IMF |
| current_account | Current account balance | Currency or % GDP | Quarterly | IMF BOP |
| npl_ratio | Non-performing loans / total loans | % | Quarterly/Semi-annual | Supervisory sources |

## 5. Geopolitical Variables

| Variable | Definition | Unit | Frequency | Potential Source |
|---|---|---|---|---|
| geopolitical_event_count | Number of recorded geopolitical events | Count | Daily | GDELT, ACLED |
| geopolitical_severity | Event severity classification | Documented score | Event-based | Event database |
| sanction_indicator | Presence of a sanctions event | Binary | Event-based | Official sanctions records |
| conflict_indicator | Presence of armed conflict event | Binary | Event-based | ACLED, UCDP |
| gpr_index | Geopolitical Risk Index | Index points | Monthly | Caldara-Iacoviello |
| epu_index | Economic Policy Uncertainty Index | Index points | Monthly | Policy Uncertainty |
| event_intensity | Aggregated event intensity | Defined score | Daily/Monthly | Derived feature |

## 6. Financial Network Variables

| Variable | Definition | Unit | Frequency | Potential Source |
|---|---|---|---|---|
| exposure_value | Financial exposure between nodes | Currency units | Quarterly | BIS, supervisory data |
| network_degree | Number of connected nodes | Count | Network snapshot | Derived |
| degree_centrality | Normalised connection count | 0-1 | Network snapshot | Derived |
| eigenvector_centrality | Importance based on connected nodes | Score | Network snapshot | Derived |
| betweenness_centrality | Share of shortest paths through a node | 0-1 | Network snapshot | Derived |
| network_density | Actual / possible edges | 0-1 | Network snapshot | Derived |
| network_stress | Aggregated network stress | Defined score | Daily/Quarterly | Derived |
| debt_rank | Network-based systemic impact measure | Defined score | Network snapshot | Derived |

## 7. Textual Intelligence Variables

| Variable | Definition | Unit | Frequency | Potential Source |
|---|---|---|---|---|
| news_sentiment | Financial or geopolitical text sentiment | Model score | Daily | Licensed news archives |
| event_category | Classified event category | Categorical | Event-based | NLP pipeline |
| entity_country | Extracted country entity | Categorical | Event-based | NLP pipeline |
| entity_institution | Extracted institution | Categorical | Event-based | NLP pipeline |
| event_severity | Model-estimated event severity | Defined score | Event-based | NLP pipeline |
| uncertainty_score | Textual uncertainty estimate | Model score | Daily | NLP pipeline |
| article_count | Relevant articles per period | Count | Daily | News corpus |

## 8. Alternative Data Variables

| Variable | Definition | Unit | Frequency | Potential Source |
|---|---|---|---|---|
| shipping_activity | Shipping movement indicator | Count/index | Daily | Licensed shipping data |
| port_congestion | Port congestion estimate | Index/Time | Daily | Shipping data provider |
| satellite_activity | Extracted activity indicator | Defined score | Variable | Licensed imagery |
| web_attention | Online attention indicator | Count/index | Daily | Permitted web data |

## 9. Target Variables

### Contagion Target

Name: contagion

Type: Binary

Values:
- 0 = No labelled contagion event
- 1 = Labelled contagion event

The operational definition must be established
before training.

### Contagion Probability

Name: contagion_probability

Type: Continuous

Range: 0 to 1

Definition:
Estimated probability of the defined contagion event
within the specified forecast horizon.

### Risk Severity

Name: risk_severity

Type: Ordinal or continuous

Definition:
Severity of the identified systemic financial stress.

The classification thresholds must be documented
and validated.

## 10. Temporal Metadata

Every observation should include:

| Field | Definition |
|---|---|
| observation_date | Date the observation refers to |
| publication_date | Date the data was published |
| availability_date | Date the data became available |
| retrieval_timestamp | Time the data was retrieved |
| revision_version | Data revision identifier |
| source_name | Original data provider |
| source_license | Applicable data licence |
| country_code | Standard country identifier |
| currency_code | ISO currency identifier |

## 11. Data Integrity Rules

1. Never use future information for historical predictions.
2. Preserve original publication timestamps.
3. Record revised and initial data releases separately.
4. Document currency conversion methodology.
5. Maintain consistent country identifiers.
6. Identify missing and stale observations.
7. Document imputation methods.
8. Maintain source-level provenance.

## 12. Point-in-Time Integrity

Macroeconomic data may be revised after publication.

A model operating at historical date t must only
use the information actually available at date t.

Example:

GDP observations published after the prediction
date must not enter the historical feature set.

The same principle applies to banking exposures,
news information and geopolitical event records.

## 13. Source and Licensing Policy

Potential providers include:

- Bank for International Settlements (BIS)
- International Monetary Fund (IMF)
- World Bank
- National central banks
- National statistical agencies
- GDELT
- ACLED
- UCDP
- Caldara-Iacoviello GPR
- Economic Policy Uncertainty database
- Authorised market data vendors

Provider access does not automatically imply
permission for redistribution.

## 14. Important Note

This is a proposed data specification.

Exact field definitions, data coverage, measurement
units and source licences must be confirmed for
each dataset before production use.

---

Copyright © Harsh Singh. All rights reserved.