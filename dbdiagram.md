Table public.labs {
  id uuid [pk, increment]

  name varchar

  is_active bool
  created_at timestamp [default: `now()`]
  updated_at timestamp
}

Table public.tests {
  id uuid [pk, increment]

  started_at timestamp
  completed_at timestamp
  comment varchar [null]

  lab_id uuid [ref: > public.labs.id]

  is_active bool
  created_at timestamp [default: `now()`]
  updated_at timestamp
}

Table indicators.indicators {
  id uuid [pk, increment]
  name varchar
  description varchar [null]

  is_active bool
  created_at timestamp [default: `now()`]
  updated_at timestamp
}

Table indicators.metrics {
  id uuid [pk, increment]

  name varchar
  description varchar [null]
  unit varchar

  is_active bool
  created_at timestamp [default: `now()`]
  updated_at timestamp
}

Table indicators.indicators_metrics {
  id uuid [pk, increment]

  indicator_id uuid [ref: > indicators.indicators.id]
  metric_id uuid [ref: > indicators.metrics.id]

  is_active bool
  created_at timestamp [default: `now()`]
  updated_at timestamp
}

Table indicators.scores {
  id uuid [pk, increment]
  score decimal

  test_id uuid [ref: > public.tests.id]
  indicator_metric_id uuid [ref: > indicators.indicators_metrics.id]

  is_active bool
  created_at timestamp [default: `now()`]
  updated_at timestamp
}

Table indicators.references {
  id uuid [pk, increment]

  min_score decimal
  max_score decimal

  indicator_metric_id uuid [ref: > indicators.indicators_metrics.id]

  is_active bool
  created_at timestamp [default: `now()`]
  updated_at timestamp
}
