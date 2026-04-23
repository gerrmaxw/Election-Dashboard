from __future__ import annotations
from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class Race(BaseModel):
    race_id: str
    state: str
    office: str
    district: Optional[str] = None
    race_name: str
    primary_date: Optional[date] = None
    source: str = "civicapi"


class Candidate(BaseModel):
    candidate_id: str
    race_id: str
    name: str
    party: Optional[str] = None
    state: str
    office: str
    district: Optional[str] = None
    incumbent: bool = False
    votes: Optional[int] = None
    vote_share: Optional[float] = None
    won: Optional[bool] = None
    margin: Optional[float] = None
    fec_committee_id: Optional[str] = None


class SpendRecord(BaseModel):
    record_id: str
    candidate_id: Optional[str] = None
    advertiser_name: str
    cycle: int = 2026
    state: str
    race_name: Optional[str] = None
    medium: str
    market: Optional[str] = None
    spend: float
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    match_source: str = "direct"      # "direct" | "fec_ie"
    confidence: float = 1.0
    source_file: Optional[str] = None


class GeoOverlap(BaseModel):
    dma_code: str
    dma_name: str
    state: str
    district: Optional[str] = None
    overlap_pct: float = Field(ge=0.0, le=1.0)


class CampaignRollup(BaseModel):
    candidate_id: str
    candidate_name: str
    party: Optional[str] = None
    state: str
    office: str
    district: Optional[str] = None
    primary_date: Optional[date] = None
    won: Optional[bool] = None
    votes: Optional[int] = None
    vote_share: Optional[float] = None
    margin: Optional[float] = None
    broadcast_spend: float = 0.0
    cable_spend: float = 0.0
    streaming_spend: float = 0.0
    digital_spend: float = 0.0
    radio_spend: float = 0.0
    mail_spend: float = 0.0
    other_spend: float = 0.0
    total_spend: float = 0.0
    tv_spend: float = 0.0
    tv_per_vote: Optional[float] = None
    total_per_vote: Optional[float] = None
    broadcast_only: bool = False
    cable_ctv_only: bool = False
    advertiser_count: int = 0
    advertisers: str = ""
